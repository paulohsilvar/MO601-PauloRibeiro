#!/bin/bash

PINPLAY="/l/disk0/work0/PauloH/Project2/pinplay-drdebug-pldi2016-3.0-pin-3.0-76991-gcc-linux"
PINBALL="/l/disk0/work0/PauloH/Project2/cpu2006_pinballs/"

for i in "$PINBALL"*; do

  BENCHMARK=${i#$PINBALL};
  DIR=$PINBALL$BENCHMARK/pinball_short.pp
  FILE=$(ls $DIR/*.address)
  NEWFILE=${FILE%".address"}

  echo "Runing " $BENCHMARK " - TLB with 4KB"

  
  ./pin -xyzzy -reserve_memory $FILE -t $PINPLAY/extras/pinplay/bin/intel64/allcache_4kb.so -o ./results/$BENCHMARK-4kb.csv -replay -replay:basename $NEWFILE -- $PINPLAY/extras/pinplay/bin/intel64/nullapp
  
  echo "Runing " $BENCHMARK " - TLB with 4MB"
  
  ./pin -xyzzy -reserve_memory $FILE -t $PINPLAY/extras/pinplay/bin/intel64/allcache_4mb.so -o ./results/$BENCHMARK-4mb.csv -replay -replay:basename $NEWFILE -- $PINPLAY/extras/pinplay/bin/intel64/nullapp

done
