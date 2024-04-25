rm -rf ./results_nt
#../Tensile/bin/Tensile -v ../tuning/hpa_bfloat16_gemm_wmma_gfx1100_streamk.yaml ./results
mkdir -p build

export HIP_VISIBLE_DEVICES="1"

fixed_size=12
echo "Running with fixed grid $fixed_size"

#TENSILE_STREAMK_FIXED_GRID=$fixed_size ../Tensile/bin/Tensile -v hpa_test.yaml ./results 
#TENSILE_STREAMK_FIXED_GRID=$fixed_size ../Tensile/bin/Tensile -v hpa_test_hhs.yaml ./results 
TENSILE_STREAMK_FIXED_GRID=$fixed_size ../Tensile/bin/Tensile -v  ./hhs_nt.yaml ./build/results_nt
