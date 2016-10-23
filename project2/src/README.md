Os arquivos criados ou modificados s�o:
	1- makefile.rules
	2- allcache_4kb.cpp
	3- allcache_4mb.cpp
	4- toy_benchmark.cpp
	5- run_project2.sh
	6- select_bench.py
	7- convert_results_to_csv.py
	8- plot_bar.py

1- makefile.rules | 2- allcache_4kb.cpp | 3- allcache_4mb.cpp | 4- toy_benchmark.cpp
	O makefile.rules faz parte do makefile, ele � respons�vel por compilar as duas pintools e gerar seus execut�veis. O allcache_4kb.cpp e o allcache_4mb.cpp s�o as duas pintools, uma com TLB de 4KB e a outra com TLB de 4MB. Esses arquivos devem estar no mesmo diret�rio.
	Como foi usado o pinplay-drdebug-pldi2016-3.0-pin-3.0-76991-gcc-linux para execu��o dos benchmarks, esses arquivos ficavam contidos no diret�rio $PIN_ROOT/extras/pinplay/examples. Para gerar os executaveis das pintools basta usar o comando make
	De acordo com a configura��o do makefile, os execut�veis das pintools est�o sendo salvas no diret�rio $PIN_ROOT/extras/pinplay/bin/intel64
	O toy_benchmark.cpp � o benchmark desenvolvido para avalia��o do ambiente.


5- run_project2.sh
	Ele � um script shell para realizar a execu��o do pinplay. Ele executa todos os benchmarks com todas as entradas. Ele j� possui a configura��o dos paths do PINPLAY e do PINBALL conforme foi utilizado. Este arquivo tem que estar no diret�rio $PIN_ROOT, onde temos o execut�vel do pin. Os resultados ser�o armazenados no diret�rio $PIN_ROOT/results, caso ele n�o exista � preciso crialo antes da execu��o do script.



6- select_bench.py
	Ele � um script em python que � responsavel por apresentar os benchmarks com suas entradas que possuem maior acesso a memoria por dados, para serem escolhidos para a avalia��o. Ele recebe como parametro os resultados .csv dos benchmarks executados. Esse script fica salvo no mesmo diretorio dos resultados dos benchmarks. para executa-lo basta chama-lo como no exemplo a seguir.
	$: ./select_bench.py *.csv	



7- convert_results_to_csv.py
	Ele � um script em python, tem como objetivo ler todos os arquivos .csv gerados como resultado da execu��o do ./run_project2.sh e gerar a tabela results.csv conforme modelo pedido para entrega do projeto. Esse script deve estar no mesmo diret�rio onde os arquivos .csv de resultado dos benchmarks escolhidos para avalia��o est�o. 
	Ele recebe como par�metro os arquivos que ser�o convertido, conforme podemos ver no exemplo a seguir.
	Exemplo de uso:
	$: ./convert_results_to_csv.py *.csv



8- plot_bar
	Ele � um script em python, tem como objetivo criar gr�ficos usando os dados dos arquivos .csv de resultados do pinplay. Ele est� configurado para apresentar os resultados dos benchmarks selecionados para avalia��o, para os benchmarks que possuem mais de uma entrada, ele utiliza a que teve melhor resultado no select_bench.py.
	Para executalo basta chama-lo:
	$: ./plot_bar






