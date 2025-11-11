
# ---------- Author: Solmaz Seyed Monir
# ---------- Dynamic Vectorization Layer ----------

class VectorizationLayer(nn.Module):
    """
    Converts irregular trajectory data (variable-length sequences)
    into a fixed-size feature–time tensor through normalization,
    binning, and projection.
    """
    def __init__(self, num_features=6, num_bins=32):
        super(VectorizationLayer, self).__init__()
        self.num_features = num_features
        self.num_bins = num_bins
        self.linear_proj = nn.Linear(num_features, num_features)

    def forward(self, x, time_index):
        """
        x: (batch_size, seq_len, num_features)
        time_index: (batch_size, seq_len) timestamps or time bins
        """
        batch_size, seq_len, _ = x.shape
        bins = torch.zeros(batch_size, self.num_bins, self.num_features, device=x.device)
        counts = torch.zeros(batch_size, self.num_bins, device=x.device)

     
        for b in range(batch_size):
            for t in range(seq_len):
                bin_idx = int((time_index[b, t] / time_index[b].max()) * (self.num_bins - 1))
                bins[b, bin_idx] += x[b, t]
                counts[b, bin_idx] += 1

        counts = counts.unsqueeze(-1).clamp(min=1.0)
        bins /= counts
        bins = self.linear_proj(bins)  # projection step
        return bins  # (batch, num_bins, num_features)



class VecLSTM(nn.Module):
    def __init__(self, num_features=6, num_bins=32, cnn_channels=64, hidden_dim=128, num_classes=5):
        super(VecLSTM, self).__init__()
        self.vectorization = VectorizationLayer(num_features, num_bins)
        self.conv1 = nn.Conv1d(num_features, cnn_channels, kernel_size=3, padding=1)
        self.bn1 = nn.BatchNorm1d(cnn_channels)
        self.lstm = nn.LSTM(cnn_channels, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, num_classes)

    def forward(self, x, time_index):
        v = self.vectorization(x, time_index)              # (B, T, F)
        v = v.permute(0, 2, 1)                             # (B, F, T)
        c = F.relu(self.bn1(self.conv1(v)))                 # CNN encoding
        c = c.permute(0, 2, 1)                             # (B, T, C)
        _, (h, _) = self.lstm(c)                           # LSTM encoding
        out = self.fc(h[-1])                               # classification head
        return out



    model = VecLSTM(num_features, num_bins=32, cnn_channels=64, hidden_dim=128, num_classes=3)
    y = model(x, t)
    print("Output logits:", y.shape)  # -> (8, 3)
