pragma circom 2.0.0;

template LabelValid() {
    // Private input: worker's label
    signal input label;

    // Public output: proof validity
    signal output isValid;

    // Constraint: label * (label - 1) == 0
    // This enforces label ∈ {0,1}
    isValid <== 1;
    label * (label - 1) === 0;
}

component main = LabelValid();
