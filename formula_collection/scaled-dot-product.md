### Scaled Dot-Product Attention

Given the queries \(Q\), keys \(K\), and values \(V\), the scaled dot-product attention is computed as follows:

1. **Dot Product of Query and Key**:
   ```math
   \text{attention\_logits} = QK^T
   ```

2. **Scaling by the Dimension of Key**:
   ```math
   \text{scaled\_attention\_logits} = \frac{\text{attention\_logits}}{\sqrt{d_k}}
   ```
   where \(d_k\) is the dimension of the keys (or queries).

3. **Applying the Softmax Function**:
   ```math
   \text{attention\_weights} = \text{softmax}(\text{scaled\_attention\_logits}) = \frac{\exp(\text{scaled\_attention\_logits})}{\sum \exp(\text{scaled\_attention\_logits})}
   ```

4. **Computing the Final Output**:
   ```math
   \text{output} = \text{attention\_weights} \cdot V
   ```

Putting it all together, the scaled dot-product attention can be summarized as:
```math
\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right) V
```
