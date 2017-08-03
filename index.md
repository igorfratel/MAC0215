---
name: Igor Fratel Santana - MAC0215
---
# 03/08/2017
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



- [X] Perguntar ao autor sobre os valores de "k" inconsistentes dados no artigo
- [X] Baixar os arquivos necessarios (sequencias fasta e anotações)
- [ ] Modificar o ROC100.py (otimizar e incluir funcionalidades)
- [ ] Rodar o Blast nas 26.197 sequências
- [ ] Rodar o NC 
- [ ] Rodar o porthoDom





