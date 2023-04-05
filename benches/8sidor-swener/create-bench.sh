#!/usr/bin/sh

nums=( 120 180 210 300 600 1000 )
PWD=`pwd`
echo "PWD=$PWD"
for num in ${nums[*]}
do
    cd "$PWD"
    text_dir="texts-$num"
    mkdir -pv "$text_dir/source"
    cd "$text_dir"
    ln -sfv ../../../assets/8sidor-swener/config.yaml .
    cd ..
    cd "$text_dir/source"
    ln -sfv "../../../../assets/texts/8sidor-mini-$num.xml" .
    cd ../..

done
