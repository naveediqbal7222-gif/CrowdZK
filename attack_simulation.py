import random
import matplotlib.pyplot as plt

# -----------------------------
# Step 1: Dataset
# -----------------------------
dataset = [1, 0, 1, 1, 0, 0, 1]  # multiple samples

attempts = 50

bc_success = []
mix_success = []
zk_success = []

# -----------------------------
# Attack Models
# -----------------------------
def attack_crowdbc(true_label):
    return true_label  # perfect leak

def attack_crowdmix(true_label, attempt):
    prob = min(0.5 + 0.01 * attempt, 0.9)
    return true_label if random.random() < prob else 1 - true_label

def attack_crowdzk(true_label):
    return random.choice([0, 1])  # no info

# -----------------------------
# Simulation
# -----------------------------
bc_correct = 0
mix_correct = 0
zk_correct = 0

for i in range(1, attempts + 1):
    for true_label in dataset:
        
        # CrowdBC
        if attack_crowdbc(true_label) == true_label:
            bc_correct += 1
        
        # CrowdMix
        if attack_crowdmix(true_label, i) == true_label:
            mix_correct += 1
        
        # CrowdZK
        if attack_crowdzk(true_label) == true_label:
            zk_correct += 1
    
    total = i * len(dataset)
    
    bc_success.append(bc_correct / total)
    mix_success.append(mix_correct / total)
    zk_success.append(zk_correct / total)

# -----------------------------
# Plot Graph
# -----------------------------
plt.figure()

plt.plot(range(1, attempts+1), bc_success, label="CrowdBC")
plt.plot(range(1, attempts+1), mix_success, label="CrowdMix")
plt.plot(range(1, attempts+1), zk_success, label="CrowdZK")

plt.xlabel("Number of Probing Attempts")
plt.ylabel("Attack Success Rate")
plt.title("Attack Success Rate vs Probing Attempts")

plt.legend()
plt.grid()

# Save figure
plt.savefig("attack_graph.png", dpi=300)

plt.show()

# -----------------------------
# Print Final Results
# -----------------------------
print("Final Attack Success Rates:")
print(f"CrowdBC: {bc_success[-1]:.2f}")
print(f"CrowdMix: {mix_success[-1]:.2f}")
print(f"CrowdZK: {zk_success[-1]:.2f}")