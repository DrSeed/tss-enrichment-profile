import os,numpy as np,matplotlib;matplotlib.use("Agg")
import matplotlib.pyplot as plt
os.makedirs("figures",exist_ok=True);os.makedirs("results",exist_ok=True)
rng=np.random.default_rng(4);pos=np.arange(-2000,2001,20)
signal=1+6*np.exp(-(pos**2)/(2*250**2))  # sharp peak at TSS
signal+=rng.normal(0,0.15,len(pos))
plt.figure(figsize=(7,4));plt.plot(pos,signal)
plt.axvline(0,ls="--",c="grey");plt.xlabel("distance from TSS (bp)");plt.ylabel("normalised signal")
plt.title("TSS enrichment profile (demo data)")
plt.tight_layout();plt.savefig("figures/demo.png",dpi=150)
open("results/summary.txt","w").write(f"TSS enrichment ~{signal.max():.1f}x\n");print("ok")