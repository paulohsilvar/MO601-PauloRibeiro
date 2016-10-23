Os arquivos criados ou modificados são:
	1- makefile.rules
	2- allcache_4kb.cpp
	3- allcache_4mb.cpp
	4- toy_benchmark.cpp
	5- run_project2.sh
	6- select_bench.py
	7- convert_results_to_csv.py
	8- plot_bar.py

1- makefile.rules | 2- allcache_4kb.cpp | 3- allcache_4mb.cpp | 4- toy_benchmark.cpp
	O makefile.rules faz parte do makefile, ele é responsável por compilar as duas pintools e gerar seus executáveis. O allcache_4kb.cpp e o allcache_4mb.cpp são as duas pintools, uma com TLB de 4KB e a outra com TLB de 4MB. Esses arquivos devem estar no mesmo diretório.
	Como foi usado o pinplay-drdebug-pldi2016-3.0-pin-3.0-76991-gcc-linux para execução dos benchmarks, esses arquivos ficavam contidos no diretório $PIN_ROOT/extras/pinplay/examples. Para gerar os executaveis das pintools basta usar o comando make
	De acordo com a configuração do makefile, os executáveis das pintools estão sendo salvas no diretório $PIN_ROOT/extras/pinplay/bin/intel64
	O toy_benchmark.cpp é o benchmark desenvolvido para avaliação do ambiente.


5- run_project2.sh
	Ele é um script shell para realizar a execução do pinplay. Ele executa todos os benchmarks com todas as entradas. Ele já possui a configuração dos paths do PINPLAY e do PINBALL conforme foi utilizado. Este arquivo tem que estar no diretório $PIN_ROOT, onde temos o executável do pin. Os resultados serão armazenados no diretório $PIN_ROOT/results, caso ele não exista é preciso crialo antes da execução do script.



6- select_bench.py
	Ele é um script em python que é responsavel por apresentar os benchmarks com suas entradas que possuem maior acesso a memoria por dados, para serem escolhidos para a avaliação. Ele recebe como parametro os resultados .csv dos benchmarks executados. Esse script fica salvo no mesmo diretorio dos resultados dos benchmarks. para executa-lo basta chama-lo como no exemplo a seguir.
	$: ./select_bench.py *.csv	



7- convert_results_to_csv.py
	Ele é um script em python, tem como objetivo ler todos os arquivos .csv gerados como resultado da execução do ./run_project2.sh e gerar a tabela results.csv conforme modelo pedido para entrega do projeto. Esse script deve estar no mesmo diretório onde os arquivos .csv de resultado dos benchmarks escolhidos para avaliação estão. 
	Ele recebe como parâmetro os arquivos que serão convertido, conforme podemos ver no exemplo a seguir.
	Exemplo de uso:
	$: ./convert_results_to_csv.py *.csv



8- plot_bar
	Ele é um script em python, tem como objetivo criar gráficos usando os dados dos arquivos .csv de resultados do pinplay. Ele está configurado para apresentar os resultados dos benchmarks selecionados para avaliação, para os benchmarks que possuem mais de uma entrada, ele utiliza a que teve melhor resultado no select_bench.py.
	Para executalo basta chama-lo:
	$: ./plot_bar






