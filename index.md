# Diário de bordo

## 20/02/2018

Arrumei o formato do output pra ficar de acordo com o sugerido na apresentação.  
Agora os scores têm precisão de 7 casas decimais.  
Adicionei a opção de estringência para as vizinhanças, além de para as proteínas.  
Adicionei  opção de pairings_filename, que especifica um arquivo para salvar as escolhas das arestas pela medida do porthodom.  
O arquivo de pairings tem o formato  
">accession1 coordenadas1 accession2 coordenadas2  
 proteina1 proteina2 similaridade  
 proteinaN proteinaM similaridade"
                                      
[comment]: <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
                              

## 17/02/2018

Tentei paralelizar uma parte do programa usando openMP, mas a versão paralelizada ficou mais lenta que a serial

[comment]: <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>

## 15/02/2018

Nos últimos dias eu discuti o projeto em reuniões, onde optamos pela implementação com listas de adjacência, realizei
otimizações no programa, gerei planilhas e gráficos de performance e me livrei da necessidade de um script em python para
parsear as vizinhanças.  

[comment]: <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>

## 06/02/2018

Tornei o projeto mais flexível. Agora cada nova medida de comparação de vizinhanças tem seu próprio arquivo com suas funções.
Isso facilita a inclusão de novas medidas.  

Implementei a versão O2 do MWM do porthodom, a medida que leva em conta a ordem das proteínas nas vizinhanças. 
Ainda não testei, só compilei.


[comment]: <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>


## 05/02/2018

Testei a biblioteca Eigen para matrizes na implementação de matriz de adjacência.  
Os resultados foram insatisfatórios, portanto não usarei ela.  
Teste no meu dataset: 
  tempo: 8m25.140s;  
  memória: heap total: 46218396398, heap peak: 2843934917, stack peak: 5392
Podemos ver que os resultados não foram muito abaixo da versão sem a biblioteca Eigen.

Na implementação de listas de adjacências, descobri que estava realizando os testes com um erro.
A implementação na verdade estava bem mais lenta para 177.463.380 acessos (194m36.399s).  
Isso se dava por conta da busca linear pelos nós em listas com muitos elementos.  
Consegui aplicar uma ideia de otimização e os novos números na planilha se referem a essa nova implementação.  

[comment]: <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>


## 31/01/2018

### Cronometrando as implementações:

```bash
time ./neighborhood_comparator --execution_mode partial --neighborhoods_filename ../data_untracked/neighborhoods_m2_exclude_filter --prot_sim_filename ../data_untracked/NC_output_m2_excluded_filter.txt --num_prot 18840 --stringency 0 --genome_comparing porthodom -o comparator_output_m2_excluded_filter
```

No notebook:

Com matriz:
real	8m4.781s
user	8m0.211s
sys	    0m1.590s

46218848558 bytes

Com lista:
real	10m23.963s
user	10m21.539s
sys	0m2.054s

43671898478 bytes

Com Union-Find:
real	12m4.486s
user	11m59.149s
sys	0m1.770s

45842340789 bytes


-------------------------------------------

Na seal:

Com matriz:
real    16m19.337s
user    15m55.240s
sys     0m23.364s

Com lista:
real    22m25.669s
user    22m13.712s
sys     0m11.400s

Com Union-Find:
real    23m32.773s
user    23m22.188s
sys     0m10.152s



[comment]: <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>



## 30/01/2018

### Teste simples de adicionar 10.000 proteínas na classe ProteinCollection e buscar a similaridade entre X pares aleatórios:

*lista de adjacência:

100.000 acessos:

notebook:
real	0m0.609s
user	0m0.606s
sys	0m0.003s


1.000.000 acessos:

notebook:
real	0m6.003s
user	0m6.003s
sys	0m0.000s


10.000.000 acessos:

notebook:
real	0m59.876s
user	0m59.873s
sys	0m0.003s


177.463.380 acessos (18840*18839/2, onde 18840 é o número de proteínas no dataset que eu criei):

notebook:
real	9m58.992s
user	9m58.980s
sys	0m0.010s

-------------------------------------------------

*matriz de adjacência:

100.000 acessos:

notebook:
real	0m0.465s
user	0m0.254s
sys	0m0.210s


1.000.000 acessos:

notebook:
real	0m2.117s
user	0m1.914s
sys	0m0.200s


10.000.000 acessos:

notebook:
real	0m16.933s
user	0m16.737s
sys	0m0.197s


177.463.380 acessos:

notebook:
real	4m54.234s
user	4m54.050s
sys	0m0.183s

-------------------------------------------------

*Union-Find


100.000 acessos:

notebook:
real	0m0.447s
user	0m0.444s
sys	0m0.003s


1.000.000 acessos:

notebook:
real	0m4.262s
user	0m4.261s
sys	0m0.000s


10.000.000 acessos:

notebook:
real	0m42.209s
user	0m42.202s
sys	0m0.007s


177.463.380 acessos:

notebook:
real	12m34.320s
user	12m34.316s
sys	0m0.003s


[comment]: <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>


## 29/01/2018

### Teste simples de adicionar X proteínas na classe ProteinCollection e buscar a similaridade de um par específico:

*lista de adjacência:

10.000 proteínas:

notebook:
real	0m0.012s
user	0m0.004s
sys	0m0.008s

seal:
real	0m0.015s
user	0m0.012s
sys	0m0.000s

1077504 bytes


100.000 proteínas:

notebook:
real	0m0.084s
user	0m0.080s
sys	0m0.003s

seal:
real	0m0.128s
user	0m0.120s
sys	0m0.004s

9776424 bytes


1.000.000 proteínas:

notebook:
real	0m1.027s
user	0m1.022s
sys	0m0.004s

seal:
real	0m1.480s
user	0m1.380s
sys	0m0.096s

108964440 bytes

-------------------------------------------------

*matriz de adjacência:

10.000 proteínas:

notebook:
real	0m0.544s
user	0m0.262s
sys	0m0.191s

seal:
real	0m0.857s
user	0m0.404s
sys	0m0.448s

801077472 bytes


100.000 proteínas:

notebook:
Processo morto por falta de memória (tenho 8GB de RAM)

seal:
real	1m19.835s
user	0m35.860s
sys	0m43.964s


1.000.000 proteínas:

seal: 
Processo morto por falta de memória após 20min

-------------------------------------------------

*Union-Find:

10.000 proteínas:

notebok:
real	0m0.018s
user	0m0.018s
sys	0m0.000s

seal:
real	0m0.023s
user	0m0.024s
sys	0m0.000s

1841216 bytes


100.000 proteínas:

notebook:
real	0m0.148s
user	0m0.148s
sys	0m0.000s

seal:
real	0m0.170s
user	0m0.156s
sys	0m0.012s

17079056 bytes


1.000.000 proteínas:

notebook:
real	0m1.898s
user	0m1.851s
sys	0m0.047s

seal:
real	0m2.924s
user	0m2.752s
sys	0m0.168s

193855088 bytes


Em seguida, pretendo rodar um teste onde, ao invés de adicionar várias proteínas e fazer uma única busca, eu adiciono as
proteínas e realizo diversas buscas. Suspeito que a implementação de matrizes tenha vantagem em relação ao tempo de execução.
Depois vou rodar o teste com o dataset que eu preparei anteriormente.

[comment]: <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>

## 23/01/2018

Script que retira do Locus.todas.Virb4.fa todas as sequências cujos ids estão em accesions_m2_exclude_filter

```bash
perl -ne 'if(/^>(\S+)/){$c=$i{$1}}$c?print:chomp;$i{$_}=1 if @ARGV' accessions_m2_exclude_filter Locus.todas.Vir
b4.fa > accessions_m2_exclude_filter.fa
```

Rodei o blast nessas proteinas 

```bash
makeblastdb -in accessions_m2_exclude_filter.fa -dbtype prot && cat accessions_m2_exclude_filter.fa | blastp -num_threads 8 -query - -db accessions_m2_exclude_filter.fa -evalue 152340 -searchsp 12901285850896 -gapopen 11 -gapextend 1 -outfmt "6 qaccver saccver bitscore qlen slen qstart qend sstart send evalue length nident" -max_target_seqs 15234 > blast_m2_excluded_filter_raw.tsv
```

Instalei o NC na seal

Rodei 
```bash
NC_standalone -f blast_m2_excluded_filter.txt -o NC_output_m2_excluded_filter.txt
```

[comment]: <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>

## 22/01/2018


Como não consegui baixar as sequências FASTA de 56 proteínas query, decidi retirar as vizinhanças que continham elas:
```bash
neighborhood_explorer --exclude queries.missing Locus.todas.Virb4.unique_m2 > Locus.todas.Virb4.unique_m2_exclude
```

```bash
neighborhood_explorer --exclude queries.missing Locus.todas.Virb4.unique_m5 > Locus.todas.Virb4.unique_m5_exclude
```

Clusterizando as queries:

```bash
mmseqs createdb queries.fa queries_DB
mkdir tmp
mmseqs cluster queries_DB queries_CLU tmp
mmseqs cluster --min-seq-id 0.9 queries_DB queries_CLU tmp
```

Extraindo representantes:

```bash
mmseqs result2repseq queries_DB queries_CLU queries_CLU_SEQ
mmseqs result2flat queries_DB queries_DB queries_CLU_SEQ queries_CLU_SEQ.fasta
```

O arquivo queries_CLU_SEQ.fasta contém os representantes das queries após a clusterização, totalizando 4319 representantes.  

Selecionando somente as vizinhanças que contenham queries presentes em queries_CLU_SEQ.fasta:
```bash
cat queries_CLU_SEQ.fa | grep ">" | cut -f 2 -d ">" > tmp_queries_representatives
neighborhood_explorer --include tmp_queries_representatives Locus.todas.Virb4.unique_m2_exclude > Locus.todas.Virb4.unique_m2_exclude_filter
neighborhood_explorer --include tmp_queries_representatives Locus.todas.Virb4.unique_m5_exclude > Locus.todas.Virb4.unique_m5_exclude_filter
```
Rodando:
```bash
less Locus.todas.Virb4.unique_m2_exclude_filter | grep "ORGANISM" | wc -l
```
Verificamos que há 4106 vizinhanças gênicas restantes, sendo que o Locus.todas.Virb4.unique original continha 28314.  
Já o Locus.todas.Virb4.unique_m5_exclude_filter possui 4095 vizinhanças  

Para rodar o Blast nessas vizinhanças filtradas, preciso construir arquivos que contenham as sequências fasta de todas as proteínas
presentes:
  
```bash
neighborhood_explorer -of accession Locus.todas.Virb4.unique_m2_exclude_filter > accessions_m2_exclude_filter
neighborhood_explorer -of accession Locus.todas.Virb4.unique_m5_exclude_filter > accessions_m5_exclude_filter
```

Pausa para pedir ajuda pro Robson

[comment]: <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>

## 19/01/2018

Consegui instalar o g++ 7.2.0 (compilando na raça) e agora o projeto funciona na seal  

Construindo um dataset razoável pra testar:  

Extraindo as queries:
```bash
neighborhood_explorer -of query Locus.todas.Virb4.unique_m2 > queries.Virb4
```

```bash
blastdbcmd -target_only -db nr -entry_batch queries.Virb4 > queries.fa
grep ">" queries.fa | cut -f 1 -d " " | cut -f 2 -d ">" | grep -v -F -w -f - queries.Virb4 > queries.missing
epost -db protein -format acc -input queries.missing | efetch -format fasta >> queries.fa
```
[comment]: <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>

## 10/01/2018

Quero testar a performance em relação a tempo de execução e consumo de memória das implementações com listas de adjacência
e matriz de adjacência, para poder excluir uma delas.  
Tentei rodar o NC primeiro, para eliminar esse overhead.  

``` bash
NC_standalone -f blast_projeto_cut_spaced.txt -o NC_output.txt
```

O processo foi morto, provavelmente porque o NC consumiu muita memória com um arquivo Blast desse tamanho.  

Resolvi diminuir o número de proteínas do conjunto de teste:
```bash
neighborhood_explorer -m 5 Locus.todas.Virb4.unique > Locus.todas.Virb4.unique_m5
```

Usei meu programa que filtra as linhas do blast cujas proteínas não estão presentes do arquivo de vizinhanças:
```bash
python parse_blast.py Locus.todas.Virb4.unique_m5 blast_projeto_cut_spaced.txt > blast_projeto_m5.txt
```
[comment]: <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>

## 09/01/2018

Implementei a versão com listas de adjacência

[comment]: <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>

## 08/01/2018

Descobri na STL do C++ o unordered_map, que soluciona um problema do unionfind de repetição de proteínas e já implementa
uma hashtable internamente. Incluí o unordered_map na implementação.  
Fiz o teste mini no UnionFind e deu certo.  
Mudei o map da versão de grafos para unordered_map também, pois permite acesso a elementos individuais em tempo praticamente constante.

Próximo objetivo: implementar a versão de grafo com lista de adjacência e testar performance pra já excluir uma implementação.

[comment]: <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>

## 04/01/2018

Terminei a implementação da versão do programa com unionfind e hashtable.  
Falta testar o funcionamento, implementar a versão com listas de adjacência nos grafos e considerar
a integração da hashtable no grafo.  
Aí pretendo fazer um grande teste com todas as versões a analisar o desempenho.

[comment]: <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>

## 20/12/2017

Implementei o UnionFind e um HashTable para proteínas.  
Pretendo usar o HashTable dentro do UnionFind, para manter o acesso aos índices do vetor do UnionFind em tempo constante, já
que as chaves são strings e não inteiros.  
Mudei o UndirectedEdgeWeightedGraph pra ProteinCollection. Isso aumenta a abstração da classe e me permite trocar as 
implementações de grafo e de union-find sem ter que alterar muito do resto do código. Pretendo integrar o union-find como
uma implementação alternativa do ProteinCollection em um novo branch do github e testar as duas implementações para 
avaliar as vantagens e desvantagens, já que o union-find é bem mais rápido mas não permite o armazenamento dos valores
de similaridade, guardando apenas relações binárias.


[comment]: <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>


## 19/12/2017

Agora o projeto suporta multiplas proteínas âncora.  
O cds das proteínas está sendo guardado com um par de números.  
O output está no formato:  
    Rickettsia sibirica AABW01000001.1 803087..834945 Rickettsia sibirica AABW01000001.1 515046..541667 0
    gênero     espécie  accession           cds  
Agora temos parsing de argumentos da linha de comando, usando [cxxopts](https://github.com/jarro2783/cxxopts).

Exemplos de execução do projeto:  

```bash
./neighborhood_comparator --help
```

```bash
./neighborhood_comparator --execution_mode full \
--neighborhoods_filename ../data/neighborhoods_mini.txt \
--prot_sim_filename NC_output_mini.txt \
--formatted_prot_filename ../data/blast_mini.txt \
--protein_comparing nc \
--num_prot 68 \
--stringency 0 \
--genome_comparing porthodom \
--output neighborhood_comparator_output_mini.txt
```

[comment]: <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>


## 17/12/2017

Consegui fazer uma versão funcional da visualização gráfica do programa, onde fazemos upload de um arquivo texto
e um gráfico de similaridade entre vizinhanças gênicas é gerado.  
[link](https://linux.ime.usp.br/~igorfratel/genomicneighborhoodvisualizer.html)
O arquivo testado foi:  
genoma1 genoma2 93  
genoma3 genoma4 0  
genoma5 genoma6 75  
genoma7 genoma8 50  

[comment]: <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>


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

Rodei o teste com 50000 sequências, que demorou 9 horas e 26 minutos.  
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





