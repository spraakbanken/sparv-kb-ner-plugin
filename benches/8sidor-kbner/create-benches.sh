#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail
if [[ "${TRACE-0}" == "1" ]]; then
    set -o xtrace
fi

if [[ "${1-}" =~ ^-*h(elp)?$ ]]; then
    echo 'Usage: ./create-benches.sh arg-one arg-two

This is an awesome bash script to make your life better.

'
    exit
fi

cd "$(dirname "$0")"

main() {
    echo do awesome stuff
    nums=( 120 180 210 300 600 1000 )
    for num in ${nums[*]}
    do
        text_dir="texts-$num"
        mkdir -pv "$text_dir/source"
        cd "$text_dir"
        ln -sfv ../../../assets/8sidor-kbner/config.yaml .
        cd ..
        cd "$text_dir/source"
        ln -sfv "../../../../assets/texts/8sidor-mini-$num.xml" .
        cd ../..

    done
}

main "$@"
