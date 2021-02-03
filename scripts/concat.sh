#!/bin/bash

# Author: Prashanth Gurunath Shivakumar
# E-mail: pgurunat@usc.edu

if [ $# != 3 ];then
  echo "Usage: $0 <LargeVec> <indomain> <output>"
  echo "Example: $0 wiki.en.vec intra-confusion.vec concat-wiki-intra-confusion.vec"
  exit 1;
fi

lv=$1
iv=$2
ov=$3

awk 'FNR==NR{if(NR==1){dim=$2;z="0";for(i=1;i<dim;i++){z=z" "0};next;}else{a[$1]=$0;next;}}{if(FNR==1){print $1,dim+$2;}else if($1 in a){d=a[$1];$1="";print d""$0;}else{w=$1;$1="";print w,z""$0 ;}}' $lv $iv | sed 's/\s\s/ /g' > $ov
