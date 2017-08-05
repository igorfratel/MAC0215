# Diário de bordo

## 05/08/2017

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
Nesse fim de semana, pretendo me dedicar a escrever a proposta de trabalho para MAC0215 e, se possível, continuar as
modificações no ROC100.py.  

- [ ] Calcular o número de pares FF e FO e bater com os valores do artigo
- [ ] Modificar o ROC100.py para rodar o NC uma única vez com o threshold mínimo
- [ ] Rodar o NC
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





