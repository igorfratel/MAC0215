# Diário de bordo

## 13/12/2017

Criei a pasta mini, onde vou fazer um teste verificável.  
Peguei as 3 primeiras vizinhanças gênicas do arquivo Locus.todas.Virb4.unique, gerando o Locus.todas.Virb4.unique_mini.  
Escrevi um programinha parse_blast.py para pegar o arquivo blast de todas as proteínas e manter somente aqueles pares onde 
ambas as proteínas estejam em Locus.todas.Virb4.unique_mini.  

Rodei o programa:
```bash
./projeto 0 ../../data/neighborhoods_mini.txt NC_output_mini.txt ../../data/blast_mini.txt nc 68 0 simple projeto_output_mini.txt
```
Pelo o que pude conferir, o programa funciona corretamente.  

No entanto, eu percebi que muitos dos pares de proteínas do meu conjunto não aparecem no Blast. Por isso, vou rodar o Blast
de novo pra garantir que todos os pares sejam computados.   
Os arquivos usados nesse teste estão na pasta data no [repositório](https://github.com/igorfratel/genome_groups) do projeto e
o teste pode ser rodado da mesma forma indicada acima.

Rodei esse script pra retirar todas as sequências fasta do meu conjunto mini, pra poder rodar o blast somente nelas
```bash
perl -ne 'if(/^>(\S+)/){$c=grep{/^$1$/}qw(EAA26069.1 EAA26070.1 EAA26071.1 EAA26072.1 EAA26073.1 EAA26074.1 EAA26075.1 EAA26076.1 EAA26077.1 EAA26078.1 EAA26079.1 EAA26080.1 EAA26081.1 EAA26082.1 EAA26083.1 EAA26084.1 EAA26085.1 EAA26086.1 EAA26087.1 EAA26088.1 EAA26089.1 EAA25784.1 EAA25785.1 EAA25786.1 EAA25787.1 EAA25788.1 EAA25789.1 EAA25790.1 EAA25791.1 EAA25792.1 EAA25793.1 EAA25794.1 EAA25795.1 EAA25796.1 EAA25797.1 EAA25798.1 EAA25799.1 EAA25800.1 EAA25801.1 EAA25802.1 EAA25803.1 EAA25804.1 EAL53886.1 EAL53887.1 EAL53888.1 EAL53889.1 EAL53890.1 EAL53891.1 EAL53892.1 EAL53893.1 EAL53894.1 EAL53895.1 EAL53896.1 EAL53897.1 EAL53898.1 EAL53899.1 EAL53900.1 EAL53901.1 EAL53902.1 EAL53903.1 EAL53904.1 EAL53905.1 EAL53906.1)}print if $c' Locus.todas.Virb4.fa > Locus.todas.Virb4.fa.mini
```
O resultado foi o arquivo Locus.todas.Virb4.fa.mini com 60 proteínas.  
Em seguida, rodei:
```bash
makeblastdb -in Locus.todas.Virb4.fa.mini -dbtype prot && cat Locus.todas.Virb4.fa.mini | blastp -num_threads 8 -query - -db Locus.todas.Virb4.fa.mini -evalue 600 -searchsp 
17002485705216400 -gapopen 11 -gapextend 1 -outfmt "6 qaccver saccver bitscore qlen slen qstart qend sstart send evalue length nident" -max_target_seqs 498457 > 
blast_mini_raw.tsv &&
```
O blast_mini_raw gerado possui somente 77 linhas, o que me leva à conclusão que realmente as proteínas não têm semelhança o
suficiente pra aparecer nos resultados.  
Fazendo as formatações necessárias, gerei um novo blast_mini.txt.  
Novamente rodei o meu programa e obtive os exatos mesmos resultados.  

Rickettsia sibirica AABW01000001.1 Rickettsia sibirica AABW01000001.1 0.933333  
Rickettsia sibirica AABW01000001.1 Rickettsia sibirica2 AABW01000001.1 0  
Rickettsia sibirica AABW01000001.1 Campylobacter upsaliensis AAFJ01000001.1 0  
Rickettsia sibirica2 AABW01000001.1 Rickettsia sibirica2 AABW01000001.1 0.933333  
Rickettsia sibirica2 AABW01000001.1 Campylobacter upsaliensis AAFJ01000001.1 0  
Campylobacter upsaliensis AAFJ01000001.1 Campylobacter upsaliensis AAFJ01000001.1 0.753846  


[comment]: <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>


## 12/12/2017

Rodei o teste com 50000 sequências e 28314 vizinhanças, que demorou 9 horas e 26 minutos.  
O comando foi o seguinte:  
```bash
./projeto 1 neighborhoods_parsed_menor.txt NC_output.txt 50000 0.5 simple projeto_genome_clustering_output.txt
```
O teste rodou sem problemas, embora seja imprático avaliar os resultados pra ver se os métodos foram aplicados corretamente.  
Principalmente porque os "splits" que eu dei nos arquivos originais não garantem que certas proteínas que aparecem nos genomas
também estejam aparecendo para o NC. Quando um par de proteínas não existe no arquivo do NC, estou atribuindo similaridade 0
a ele.  

Comecei a brincar com o Cytoscape para gerar os grafos de similaridade. Pretendo manter essa parte do projeto na minha
[homepage](https://linux.ime.usp.br/~igorfratel/genomicneighborhoodvisualizer.html)

A fim de verificar a corretude do programa, realizarei um teste menor cujos resultados eu possa conferir. 
Além disso, eu acho que o programa está consumindo muita memória, por isso vou fazer uma versão que implementa
os grafos usando listas de adjacência ao invés de matrizes.


[comment]: <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>


## 30/11/2017

Tentei rodar o NC no arquivo de blast gerado a partir do Locus.todas.virb4.fa, mas após 3 dias o processo foi cancelado por
falta de memória. Vou rodar um teste com menos sequências.  

Rodei o seguinte comando para dividir o arquivo em arquivos de 100000 linhas:
```bash
split -l 100000 Locus.todas.Virb4.fa 

```

Escolhi o arquivo "xab" para ser meu conjunto de sequências. Ele contém 50000 sequências e 12465665 resíduos  

Rodei:  
```bash
makeblastdb -in xab -dbtype prot && cat xab | blastp -num_threads 8 -query - -db xab -evalue 500000 -searchsp 
155392803892225 -gapopen 11 -gapextend 1 -outfmt "6 qaccver saccver bitscore qlen slen qstart qend sstart send evalue length nident" -max_target_seqs 50000 > 
blast_projeto_menor.tsv &&
```

Cortei o Locus.todas.Virb4.unique em 100000 linhas também e escolhi o arquivo "xaa".
Rodei o parse_neighborhood.py no xaa e gerei o arquivo "neighborhoods_parsed_menor.txt"

Quando o blast rodar pretendo executar o seguinte:

```bash
./projeto 0 neighborhoods_parsed_menor NC_output.txt blast_projeto_menor_cut_spaced.txt nc 50000 0.5 simple

```

[comment]: <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>


## 24/11/2017

Durante a semana me reuni com o Alan e fiz diversas mudanças no programa de acordo com o que discutimos nessas reuniões.  
Pretendo marcar mais uma reunião para ver a última parte do programa.  
Após isso, preciso fazer um teste grande (com o virb4, preferencialmente) e se tudo der certo acho que posso partir para a parte de visualização.

[comment]: <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>


## 20/11/2017

Implementei a classe de grafo como uma template para que possa ser usada com qualquer tipo de dados.  

Fiz diversas melhorias no programa e criei um novo branch "no_components" no github, onde o protein_clustering
já não retorna uma lista de adjacências mas sim o próprio grafo. Isso pode acarretar em uma melhoria significativa 
no tempo de execução e permitir uma granularidade mais fina na execução do MWM. No entanto, a segunda afirmação ainda precisa
ser testada. Os pesos entre as proteínas continuam binários, mas com essa mudança há várias formas de alterar isso, que precisam
ser discutidas.

Preciso rodar o NC_Standalone no arquivo blast_projeto_cut_spaces.txt, para poder testá-lo no meu programa.


[comment]: <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>


## 06/11/2017

Arrumei os erros do programa e meu pequeno teste para dois genomas com duas proteínas cada deu certo.

O objetivo é que o teste rode com o comando a seguir, porém o output não é capturado:  
```bash
python main.py -n teste.parsed.unique -s teste.sim -m 4 -t 0.3
```  

Então eu chamei o programa em C++ diretamente com o comando:
```bash
reset && make && ./projeto 1 teste.parsed.unique teste.sim 4 1 simple
```
Onde 4 é o número de proteínas e 0.3 é a estringência do agrupamento de proteínas
Os arquivos teste.parsed.unique, teste.unique e teste.sim estão disponíveis do repositório do [projeto](https://github.com/igorfratel/genome_groups)

Falta documentar, limpar melhor o código, fazer algumas otimizações e testar mais.

[comment]: <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>

## 29/10/2017

O que eu fiz desde o último post:  
Passei o projeto para c++, deixando apenas uma casca em python que lida com a lógica dos parâmetros.  
O programa compila, mas ainda não foi testado.  
Falta documentar, fazer algumas poucas melhorias e implementar o agrupamento das vizinhanças (por enquanto só imprimo a
similaridade entre elas).  

Utilizando o arquivo Locus.todas.Virb4.fa rodei o Blast para posteriormente rodar o NC.


```bash
grep ">" -o Locus.todas.Virb4.fa | wc -l
```
numero de sequencias: 498457  

```bash
awk '!/>/' Locus.todas.Virb4.fa | wc -m -
```
numero de caracteres ignorando as linhas com ">" (mas contando os newlines): 130393580  

```bash
makeblastdb -in Locus.todas.Virb4.fa -dbtype prot && cat Locus.todas.Virb4.fa | blastp -num_threads 8 -query - -db Locus.todas.Virb4.fa -evalue 4984570 -searchsp 
17002485705216400 -gapopen 11 -gapextend 1 -outfmt "6 qaccver saccver bitscore qlen slen qstart qend sstart send evalue length nident" -max_target_seqs 498457 > 
blast_projeto.tsv &&
```
[comment]: <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>

## 18/10/2017

Implementei o protein_grouping.cpp e comecei o genome_grouping.cpp.

- [ ] Parsear o arquivo das vizinhanças gênicas 

[comment]: <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>

## 13/10/2017

Decidi usar o algoritmo para encontrar os componentes conexos de um grafo para agrupar as proteínas ao invés do union find.
O motivo é que dessa forma eu consigo filtrar os grupos por peso das arestas.  
Implementei a classe UndirectedEdgeWeightedGraph que contém o método connected_components() contendo o algoritmo citado.

O algoritmo que resolve o MWM em tempo n^3 é conhecido como algoritmo húngaro. Tive dificuldade para entendê-lo e não sei se
vou conseguir implementá-lo, mas é um dos objetivos.

- [ ] Parsear os arquivos de entrada
- [ ] Implementar um MWM para as vizinhanças
- [ ] Testar todo o processo com os arquivos de input

[comment]: <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>

## 12/10/2017

Escrevi o arquivo GenomicNeighborhood.cpp contendo a classe GenomicNeighborhood, correspondente
a cada "bloco" do arquivo de entrada.

- [ ] Implementar um Union-Find para agrupar as proteínas
- [ ] Parsear os arquivos de entrada
- [ ] Implementar um MWM para as vizinhanças
- [ ] Talvez seja necessário implementar ou encontrar uma biblioteca de grafos (inclusive para o MWM)
- [ ] Testar todo o processo com os arquivos de input

[comment]: <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>

## 07/10/2017

Arrumei o MWM para duas vizinhanças gênicas.

- [ ] Implementar a clusterização
- [ ] Expandir para n vizinhanças gênicas

[comment]: <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>

## 25/09/2017

Modifiquei o protein_clustering para simplesmente criar um dicionário onde as chaves são pares
de proteínas e o valor é o NC-score entre elas.    
Comecei o genome_clustering, que agora calcula a similaridade entre duas sequências de proteínas utilizando o
método do maximal weighted matching visto no artigo do porthoDom, onde o peso das arestas do grafo é dado
pelo dicionário mencionado acima. Ainda há melhorias a serem feitas.  
**Nota**: preciso de um exemplo real de input para o programa.  

- [ ] Aprimorar o MWM
- [ ] Utilizar o MWM para clusterização de várias sequências

[comment]: <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>

## 18/09/2017

Substitui o os.system que estava rodando o NC_standalone pelo subprocess.run, que é o recomendado.

[comment]: <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>

## 04/09/2017

Implementei a função protein_clustering de forma simples: Recebendo o input do NC, ela considera que dois pares de proteínas
presentes no input formam uma aresta de um grafo. No final, escrevo todos os componentes conectados do grafo em um arquivo,
pois eles serão os clusters de proteínas.   
Utilizei a biblioteca Networks.  
- [ ] Implementar uma medida simples de agrupamento de vizinhanças gênicas para ter uma versão protótipo do programa

[comment]: <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>

## 31/08/2017

Terminei a lógica dos argumentos, isto é, as combinações válidas de argumentos para a execução do programa.
O programa pode ser executado a partir de qualquer ponto: identificação de homologia, clustering de proteínas, clustering de vizinhanças gênicas.

- [X] Definir um padrão para o input do programa
- [X] Terminar a verificação da validade dos parâmetros passados pro programa
- [X] Incluir a lógica de ver se uma combinação de parâmetros é válida para execução
- [ ] Implementar o agrupamento de proteínas padrão usando o NC
- [ ] Encontrar uma medida de agrupamento de vizinhanças gênicas

[comment]: <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>

## 28/08/2017
Li as respostas dadas pelo Robson e modifiquei os parâmetros do programa com base nelas
### Respostas

* Entrada:  
  - arquivo1: contém linhas do tipo “regiao_1 locus_tag_1...locus_tag_n”
  - arquivo2 contém “locus_tag fasta_sequence”
  - nota: pode haver mais de uma região por genoma

* Clusterização e homologia:   
Toda sequência do mesmo grupo é homóloga das outras desse grupo mas pode não ser homóloga e sem dúvida é menos similar às proteínas de outros grupos.

* Entrada para o agrupamento:  
É razoável oferecer a opção de carga dos arquivo com os bitscores. Posso implementar assim agora mas vamos querer adicionar a capacidade de cálculo dos bitscores depois (não necessariamente usando BLAST).

* Parâmetros para o agrupamento:  
O usuário deve ter a opção de fornecer mas deve ser definido um valor padrão (default).
Qual valor vamos ver depois... mas podemos começar com 0.005)

* Opções de execução:  
  - Opção 1: O usuário fornece as proteínas já clusterizadas em um arquivo (eg: arquivo de duas colunas “proteina cluster_id”)
  - Opção 2: O usuário fornece pares de proteínas e medidas de similaridade calculadas entre eles com um método qualquer   externo ao meu programa. O trabalho seria clusterizar.
  - Opção 3: O usuário fornece as proteínas e escolhe um método de detecção de homologia de proteínas(dentro dos disponíveis no meu programa?). O trabalho seria aplicar o método e depois clusterizar.

* Âncoras:  
Na entrada discutida em (1) essa informação (quem é o âncora) deverá ser fornecida, seja numa segunda coluna ou (mais provável) com uma marcação como um * ou [].


- [X] Definir um padrão para o input do programa
- [ ] Terminar a verificação da validade dos parâmetros passados pro programa
- [ ] Incluir a lógica de ver se uma combinação de parâmetros é válida para execução
- [ ] Implementar o agrupamento de proteínas padrão usando o NC
- [ ] Encontrar uma medida de agrupamento de vizinhanças gênicas

[comment]: <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>

## 22/08/2017
Fiz algumas poucas alterações no [programa](https://github.com/igorfratel/genome_groups) e pensei sobre a modelagem do problema, implementação e input.  
Pode ser útil: [PyCluster](http://bonsai.hgc.jp/~mdehoon/software/cluster/software.htm#pycluster)  

### Perguntas
1. O arquivo de banco de dados será o único arquivo de input ou ele conterá as sequências fasta enquanto outro arquivo
contém os genomas e as ids das proteínas? (eg: arquivo1 contém linhas do tipo "genoma_1 protein_id_1...protein_id_n" enquanto
o arquivo2 contém "protein_id fasta_sequence")

2. Como diferenciamos detecção de homologia e clusterização de proteínas? O usuário escolhe ambos ou a clusterização é interna ao meu programa?

3. No caso do NC, temos que rodar o Blast antes. O usuário fornece as sequências fasta e meu programa deve rodar o blast em todas as proteínas e depois rodar o NC? Parece demorado. Outros métodos podem exigir outros tipos de pré-processamento, então não seria melhor que o usuário já fornecesse os arquivos no formato certo para o método de detecção de homologia de proteínas que ele quer utilizar?
(eg: se o método escolhido for o NC, o usuário deve fornecer um arquivo "protein1 protein2 bitscore"). 

4. O usuário escolhe o threshold dos métodos de agrupamento de proteínas ou usamos um default? (No caso do nc, 0.005).

5. Podem existir essas opções?
    * Opção 1: O usuário fornece as proteínas já clusterizadas em um arquivo (eg: arquivo de duas colunas "proteina cluster_id")
    * Opção 2: O usuário fornece pares de proteínas e medidas de similaridade calculadas entre eles com um método qualquer externo ao meu programa. O trabalho seria clusterizar.
    * Opção 3: O usuário fornece as proteínas e escolhe um método de detecção de homologia de proteínas(dentro dos disponíveis no meu programa?). O trabalho seria aplicar o método e depois clusterizar.
6. Qual o output do programa que encontra os genes âncora nos fragmentos de genoma? Como ele poderia se relacionar com o input desse programa? 

### To-do
- [ ] Definir um padrão para o input do programa
- [ ] Implementar o agrupamento de proteínas padrão usando o NC
- [ ] Encontrar uma medida de agrupamento de vizinhanças gênicas

[comment]: <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>

# 21/08/2017
Planejo começar o programa, lidando com as opções de input do usuário.   

Defini como input para o programa (no arquivo main.py) as seguintes opções:
* -p or --protein_clustering (Método de agrupamento de proteínas. O padrão é o neighborhood correlation)
* -g or --genomic_clustering (Método de agrupamento de vizinhanças gênicas. Preciso pensar em um padrão)
* -v or --visualization (Forma de visualizar os dados. Vizinhanças(1), grafos(2) e/ou conjuntos(3). O padrão é (1))
* -d or --database_file (Arquivo texto usado como banco de dados. Não há padrão)

Estudei a biblioteca argparse do python e consegui gerar as funcionalidades desejadas.  
O programa se encontra no seguinte [repositório](https://github.com/igorfratel/genome-groups).

- [ ] Implementar o agrupamento de proteínas padrão usando o NC
- [ ] Encontrar uma medida de agrupamento de vizinhanças gênicas

[comment]: <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>

## 17/08/2017

Em reunião, percebemos que eu não normalizei o eixo x das curvas ROC geradas. Esse é o motivo para que a área sob a curva tenha 
dado um resultado tão diferente do apresentado no artigo.  
Normalizando:  
- Conjunto ALL: 0.00326420045135/0.004 = 0.816050113, contra os 0.8148 mostrados no artigo
- Conjunto ALL-Kin: aprox 0.00324454687756/0.0375= 0.865212501, contra os 0.8353 mostrados no artigo 

Seguem curvas ROC e ROC-scores para outras três famílias:    
![Alt text](images/roc_adam_generated.png?raw=true "Curva ROC 3")
ADAM 0.00195918771704/0.0026 = 0.753533737, contra 1 do artigo.
![Alt text](images/roc_kinase_generated.png?raw=true "Curva ROC 4")
Kinase 0.00329258221483/0.004 = 0.823145554, contra 0.8362 do artigo
![Alt text](images/roc_acsl_generated.png?raw=true "Curva ROC 5")
ACSL: 1, idêntico ao artigo

Dessa forma, observamos que os resultados são extremamente próximos aos do artigo, exceto pela família ADAM.  
Dou por encerrada a etapa de reproduzir os dados do artigo.

[ ] Escrever as bases para o programa de agrupamento de vizinhanças gênicas


[comment]: <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
## 12/08/2017 e 13/08/2017

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
![Alt text](images/roc_all_generated.png?raw=true "Curva ROC 1")
Esse gráfico está condizente com o que é apresentado no artigo. 

Calculando a area sob a curva desse gráfico obtive 0.00326420045135 com a função trapz do pacote numpy. Esse valor é condizente com o gráfico, porém é muito diferente do valor obtido pelo autor de 0.8148. Mandei um email para o autor perguntando a respeito disso.

Em suma, consegui reproduzir os gráficos mas não o score gerado por eles.
Segue outro gráfico gerado, dessa vez usando o conjunto All-kin (todas as proteínas exceto kinases).
O gráfico está extremamente semelhante ao apresentado no artigo.
![Alt text](images/roc_allkin_generated.png?raw=true "Curva ROC 2")

Embora não tenha conseguido gerar os scores, esses gráficos indicam alta sensibilidade e especificidade na detecção de
pares homólogos, segundo minha análise.

-[ ] Discutir em reunião os próximos passos

[comment]: <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>


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





