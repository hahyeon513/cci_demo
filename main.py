#%%
import argparse
from GCT import main as gct_main
from SVR import main as svr_main

def main(data_path, output_path):
   
    # SVR 모델 실행
    print("Running SVR model...")
    svr_main(data_path, output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_path', type=str, required=True)
    parser.add_argument('--output_path', type=str, required=True)
    args = parser.parse_args()
    
    main(args.data_path, args.output_path)

# %%
