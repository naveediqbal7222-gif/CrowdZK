import hashlib
import os

# -----------------------------
# Helper: Hash function
# -----------------------------
def hash_data(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

# -----------------------------
# Step 1: Commitment (Prover side)
# -----------------------------
def generate_commitment(secret_value: int):
    """
    Prover commits to a value without revealing it.
    """
    # Random nonce (hides the value)
    nonce = os.urandom(16)

    # Combine value + nonce
    data = str(secret_value).encode() + nonce

    commitment = hash_data(data)

    return commitment, nonce


# -----------------------------
# Step 2: Proof Generation
# -----------------------------
def generate_proof(secret_value: int, nonce: bytes):
    """
    Prover reveals proof (value + nonce)
    """
    return {
        "value": secret_value,
        "nonce": nonce
    }


# -----------------------------
# Step 3: Verification (Verifier side)
# -----------------------------
def verify_proof(commitment: str, proof: dict) -> bool:
    """
    Verifier checks consistency without prior knowledge
    """
    value = proof["value"]
    nonce = proof["nonce"]

    data = str(value).encode() + nonce
    computed_commitment = hash_data(data)

    return computed_commitment == commitment


# -----------------------------
# Example Usage
# -----------------------------
if __name__ == "__main__":
    # Secret label (0 or 1)
    secret = 1

    # Prover commits
    commitment, nonce = generate_commitment(secret)

    print("Commitment:", commitment)

    # Later: prover reveals proof
    proof = generate_proof(secret, nonce)

    # Verifier checks
    result = verify_proof(commitment, proof)

    print("Proof valid:", result)