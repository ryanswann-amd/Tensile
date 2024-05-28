#!/bin/bash
now=$(date +%F_%H-%M-%S)
results_dir="~/tuning_files/data/phantom/"

tag="hgemmoneproblem"
#cp f8gemm_oneproblem.yaml ~/tuning_files/data/phantom/tuning_$now\_$tag.yaml
for num in $(seq 0 16); do
../../Tensile/bin/Tensile ./yaml_files/hgemm_oneproblem_$num.yaml results_$tag\_$num | tee ./exploration_results/$tag\_$num\_$now.csv || true
done
