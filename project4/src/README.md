1- Os arquivos do simulador que foram alterados são os sequintes:

	./sniper-6.1/common/core/memory_subsystem/fast_nehalem/fast_cache.h
	./sniper-6.1/common/core/memory_subsystem/fast_nehalem/memory_manager.h
	./sniper-6.1/common/core/core.cc
	./sniper-6.1/common/core/memory_subsystem/cache/pr_l2_cache_block_info.cc
	./sniper-6.1/common/core/memory_subsystem/mem_component.h
	./sniper-6.1/common/core/memory_subsystem/memory_manager_base.h
	./sniper-6.1/common/core/memory_subsystem/parametric_dram_directory_msi/cache_cntlr.cc
	./sniper-6.1/common/core/memory_subsystem/parametric_dram_directory_msi/memory_manager.cc
	./sniper-6.1/common/core/memory_subsystem/parametric_dram_directory_msi/memory_manager.h
	./sniper-6.1/common/performance_model/hit_where.h
	./sniper-6.1/tools/gen_topology.py
	./sniper-6.1/tools/mcpat.py

  Os arquivos derivados do diretorio /common estão dentro do zip chamado common.zip
  Os arquivos derivados do diretorio /tools estão dentro do zip chamado tools.zip


2- Os arquivos com extensão .out são os arquivos de saída gerados pelo simulador sniper, com dados sobre a simulação.
Quantidade de instruções executadas, IPC, Acessos a Cache, etc...

3- Os arquivos com extensão .csv contém os valores de IPC para cada cenário de simulação,
eles são lidos pelo script em python para gerar o gráfico de resultado.

4- O arquivo plot_project4.py é um script em python que utiliza de bibliotecas de geração de gráficos
para construir o gráfico de resultados baseado nos dados contidos nos arquivos mensionados no item 3.

5- O diretorio config possui os arquivos de configuração usados na chamado do simulador sniper,
nesses arquivos possuem a configuração do processador. Os arquivos que são passados para o simulador
são os que tem o prefixo "gainestown", ele já inclui os com prefixo "nehalem". Nos arquivos com prefixo
"nehalem" estão as configurações para a trace cache que é igual para os dois e as configurações de brand
predictor que altera 1bit e o usado no pentium_m.

6- Para compilar e simular o sniper foi seguido o tutorial que se encontra no link:
http://snipersim.org/documents/sniper-manual.pdf

É preciso ter baixado tanto o simulador sniper quanto os benchmarks por eles fornecidos.

Para simular o sniper com um benchmark também foi seguido pelo manual, mas exatamente pelos comandos:

$ cd  benchmarks
$ export  SNIPER_ROOT =/path/to/sniper
$ export  BENCHMARKS_ROOT=$(pwd)
$ make
$ ./run -sniper  -p splash2 -fft -i small -c gainestown

Para simular com o cenário de brand predictor de 1 bit, alteramos o arquivo de configuração na linha de comando, conforme exemplo a seguir:

$ ./run -sniper  -p splash2 -fft -i small -c gainestown_onebit



