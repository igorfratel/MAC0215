# Diário de bordo

# 12/08/2017 e 13/08/2017

Calculei o número de pares FF e FO com o seguinte script e de acordo com a fórmula que o autor do artigo me mandou por email:
``` python
families = [10, 44, 81, 31, 32, 77, 38, 7, 12, 8, 14, 12, 44, 906, 56, 22, 46, 44, 38, 55]
FF = 0
FO = 0
for i in families:
	FF += i*i
	FO += i*(26197 - i)
print("FF = " + str(FF) + "  " + "FO = " + str(FO) + "\n")
```
Os número de pares FF e FO foi igual ao mostrado no artigo.  

Separei o programa ROC100.py para facilitar a depuração, pois não estava obtendo os valores esperados.    
Segue a sequência de passos realizada:  
Tenho o **nc_results.txt** obtido anteriormente, contendo os NC-scores para os pares de proteínas. Também tenho o arquivo **curated_set.dat**, obtido no site do Neighborhood Correlation, que consiste na classificação em famílias das 1577 proteínas do benchmark.  
Rodei o script **classifier.py**, que gera um arquivo **nc_results_classified.txt** contendo a classificação dos pares de proteínas em falsos positivos (FP) ou verdadeiros positivos(TP). Se duas proteínas possuem a mesma família de acordo com o curated_set.dat, elas são TP. Caso elas tenham famílias diferentes ou não estejam presentes no curated_set.dat, são consideradas FP.  
Em seguida, ordenei o arquivo nc_results_classified.txt em ordem decrescente de NC-score usando o seguinte comando:  
``` bash
sort -g -r -k 3,3 nc_results_classified.txt > nc_results_classified_sorted.txt
```
A partir de agora, o único arquivo usado será o nc_results_classified_sorted.txt. Assumo que até aqui tudo está certo.  
Agora vou contar, a partir da primeira linha, os "FP" que aparecerem. Quando minha contagem chegar em 100*k com k = 1577, eu terei encontrado o threshold mínimo.  

> The performance of each method was assessed via the ROC-nscore (Table 3), which represents both false positives and false negatives (see Methods). ROC-n is the area under the Receiver Operating Characteristic (ROC) curve comprised of the top ranking pairs up to the first n false positives. We used n= 100k, where k is family size, corresponding to 100 false positives per query.  

O threshold encontrado pelo meu programa **fp_counter.py** foi **0.0935232293278493**, na linha "Q8IV61 Q9ES74 0.0935232293278493 FP".  
Copiei as linhas com o threshold >= 0.0935232293278493 para o arquivo **nc_results_classified_sorted_cut.txt**.  
Recapitulando, o arquivo nc_results_classified_sorted_cut.txt contém os pares de proteínas com maior NC-score até os primeiros 157.700 falsos positivos. Os pares estão classificados em FP e TP.  

Agora eu suponho ter todos os dados necessários para gerar a curva ROC100k e o ROC100k score.  

Criei o programa **roc_curve.py**, que gerou a seguinte curva ROC com o conjunto de All de famílias:
[comment]: 
Esse gráfico está condizente com o que é apresentado no artigo. 

Calculando a area sob a curva desse gráfico obtive 0.00326420045135 com a função trapz do pacote numpy. Esse valor é condizente com o gráfico, porém é muito diferente do valor obtido pelo autor de 0.8148. Mandei um email para o autor perguntando a respeito disso.

Em suma, consegui reproduzir os gráficos mas não o score gerado por eles.
Segue outro gráfico gerado, dessa vez usando o conjunto All-kin (todas as proteínas exceto kinases).
O gráfico está extremamente semelhante ao apresentado no artigo.

[comment]: 

Embora não tenha conseguido gerar os scores, esses gráficos indicam alta sensibilidade e especificidade na detecção de
pares homólogos, segundo minha análise.

-[ ] Discutir em reunião os próximos passos

[comment]: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 05/08/2017

Modifiquei o ROC100.py para gerar arquivos com as suas classificações dos pares de proteínas em verdadeiros e falsos positivos.  
Comecei a tarefa de "Modificar o ROC100.py para rodar o NC uma única vez com o threshold mínimo".  
Rodei o blastp nas 26.197 sequências, gerando o arquivo **combined_blast_results.tsv**. Para isso, utilizei o seguinte comando:  
``` bash
makeblastdb -in seq_set_79.fasta  -dbtype prot && \
cat seq_set_79.fasta | blastp -num_threads 8 -query - \
-db seq_set_79.fasta -evalue 261970 -searchsp 198061066055889 \
-gapopen 11 -gapextend 1 \
-outfmt "6 qaccver saccver bitscore qlen slen qstart qend sstart send evalue length nident" \
-max_target_seqs 261970 > combined_blast_results.tsv
```
Onde o **evalue** é 10 vezes o número de sequências e **searchsp** é o número de resíduos ao quadrado, segundo o README do
NC_standalone.  
Segundo o artigo, o número de resíduos é 14.073.417. 

Formatei o **combined_blast_results.tsv** de forma a funcionar como input para o NC_standalone. O novo arquivo se chama
**combined_blast_results_ready.txt**  
Rodei o NC_standalone utilizando o seguinte comando:  
``` bash
NC_standalone -f combined_blast_results_ready.txt -o nc_results.txt --nc_thresh -1000
```
  
Nesse fim de semana, pretendo me dedicar a escrever a proposta de trabalho para MAC0215 e, se possível, continuar as
modificações no ROC100.py.  

- [ ] Calcular o número de pares FF e FO e bater com os valores do artigo
- [ ] Modificar o ROC100.py para rodar o NC uma única vez com o threshold mínimo
- [X] Rodar o NC
- [X] Perguntar ao autor sobre os valores de “k” inconsistentes dados no artigo
- [X] Baixar os arquivos necessarios (sequencias fasta e anotações)
- [X] Fazer com que o ROC100.py gere um arquivo com as suas classificações de verdadeiros e falsos positivos
- [X] Rodar o Blast nas 26.197 sequências

[comment]: <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>


## 03/08/2017
Mandei um email para um dos autores(jacob@jjoseph.org) do [artigo](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000063)
do Neighborhood Correlation questionando sobre valores conflitantes de **k** para o cálculo do *ROC100k score*

Baixei os seguintes arquivos do site do [Neighborhood Correlation](http://neighborhoodcorrelation.org/):
- **curated_set.dat**: contém os ids das 1577 proteínas do benchmark acompanhadas de suas respectivas famílias;
- **seq_set_79.fasta**: contém as sequências fasta das 26.197 proteínas usadas no estudo;

A primeira coisa que fiz foi verificar se as proteínas no arquivo **curated_set.dat** são um subconjunto do arquivo
**seq_set_79.fasta** utilizando o seguinte código executado na bash:

```bash
grep seq_set_79.fasta -e ">" > seq_set_79_ids.txt
for i in seq_set_79_ids.txt;
do cut -c 2- $i > seq_set_79_ids_temp.txt;
done
cut -f 1 -d " " curated_set.dat > curated_set_ids.dat
sort curated_set_ids.dat > curated_set_ids_sorted.dat
sort seq_set_79_ids_temp.txt > seq_set_79_ids_sorted.txt
diff seq_set_79_ids_sorted.txt curated_set_ids_sorted.dat 
```
Analisando o output do commando `diff` podemos ver que a hipótese do subconjunto é verdadeira.


### Tasklist
* [X] Perguntar ao autor sobre os valores de "k" inconsistentes dados no artigo
- [X] Baixar os arquivos necessarios (sequencias fasta e anotações)
- [ ] Calcular o número de pares FF e FO e bater com os valores do artigo
- [ ] Fazer com que o ROC100.py gere um arquivo com as suas classificações de verdadeiros e falsos positivos
- [ ] Modificar o ROC100.py para rodar o NC uma única vez com o threshold mínimo
- [ ] Rodar o Blast nas 26.197 sequências
- [ ] Rodar o NC 
- [ ] Rodar o porthoDom





