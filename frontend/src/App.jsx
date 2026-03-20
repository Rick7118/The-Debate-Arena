import { useState } from "react";

export default function App() {
  const [topic, setTopic] = useState("");
  const [rounds, setRounds] = useState(3);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  async function startDebate() {
    if (!topic.trim()) return;
    setLoading(true);
    setResult(null);
    const res = await fetch("http://127.0.0.1:8000/debate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ topic, rounds }),
    });
    const data = await res.json();
    setResult(data);
    setLoading(false);
  }

  return (
    <div style={styles.page}>
      <div style={styles.masthead}>
        <span style={styles.mastheadTitle}>The Debate Arena</span>
        <span style={styles.mastheadSub}>AI · Multi-agent · {rounds} rounds</span>
      </div>

      <div style={styles.topicSection}>
        <div style={styles.label}>Tonight's motion</div>
        <div style={styles.inputRow}>
          <input
            style={styles.input}
            value={topic}
            onChange={(e) => setTopic(e.target.value)}
            placeholder="Enter a debate topic..."
          />
          <button style={styles.button} onClick={startDebate} disabled={loading}>
            {loading ? "Debating..." : "Debate →"}
          </button>
        </div>
      </div>

      {loading && <div style={styles.loadingText}>Agents are arguing...</div>}

      {result && (
        <>
          {result.rounds.map((r) => (
            <div key={r.round}>
              <div style={styles.roundHeader}>
                <span style={styles.roundLabel}>Round {r.round}</span>
                <div style={styles.roundLine} />
              </div>
              <div style={styles.debateGrid}>
                <div style={styles.agentCol}>
                  <div style={styles.tagFor}>For</div>
                  <p style={styles.agentText}>{r.for}</p>
                </div>
                <div style={{ ...styles.agentCol, borderLeft: "1px solid #111" }}>
                  <div style={styles.tagAgainst}>Against</div>
                  <p style={styles.agentText}>{r.against}</p>
                </div>
              </div>
            </div>
          ))}

          <div style={styles.verdictBox}>
            <div style={styles.verdictLabel}>Judge's verdict</div>
            <p style={styles.verdictText}>{result.verdict}</p>
          </div>
        </>
      )}
    </div>
  );
}

const styles = {
  page: { maxWidth: 800, margin: "0 auto", padding: "2rem 1.5rem", fontFamily: "Georgia, serif", background: "#fff", color: "#111", minHeight: "100vh" },
  masthead: { borderTop: "3px solid #111", borderBottom: "1px solid #111", padding: "0.75rem 0", marginBottom: "2rem", display: "flex", justifyContent: "space-between", alignItems: "center", gap: 24 },
  mastheadTitle: { fontSize: 20, fontWeight: 700, letterSpacing: -1, whiteSpace: "nowrap" },
  mastheadSub: { fontFamily: "Courier New, monospace", fontSize: 11, color: "#666", textTransform: "uppercase", letterSpacing: 2, textAlign: "right" },
  topicSection: { marginBottom: "2rem" },
  label: { fontFamily: "Courier New, monospace", fontSize: 10, textTransform: "uppercase", letterSpacing: 3, color: "#888", marginBottom: 6 },
  inputRow: { display: "flex", border: "1.5px solid #111" },
  input: { flex: 1, padding: "12px 16px", fontFamily: "Georgia, serif", fontSize: 15, border: "none", outline: "none", color: "#fff", background: "#111" },
  button: { padding: "12px 24px", background: "#111", color: "#fff", fontFamily: "Courier New, monospace", fontSize: 11, textTransform: "uppercase", letterSpacing: 2, border: "none", cursor: "pointer" },
  loadingText: { fontFamily: "Courier New, monospace", fontSize: 12, color: "#888", textAlign: "center", padding: "2rem 0", letterSpacing: 2, textTransform: "uppercase" },
  roundHeader: { display: "flex", alignItems: "center", gap: 12, marginBottom: "1rem", marginTop: "1.5rem" },
  roundLabel: { fontFamily: "Courier New, monospace", fontSize: 10, textTransform: "uppercase", letterSpacing: 3, color: "#888", whiteSpace: "nowrap" },
  roundLine: { flex: 1, height: 1, background: "#ddd" },
  debateGrid: { display: "grid", gridTemplateColumns: "1fr 1fr", border: "1.5px solid #111", marginBottom: "1rem" },
  agentCol: { padding: "1.25rem" },
  tagFor: { fontFamily: "Courier New, monospace", fontSize: 9, textTransform: "uppercase", letterSpacing: 3, background: "#111", color: "#fff", display: "inline-block", padding: "2px 8px", marginBottom: 10 },
  tagAgainst: { fontFamily: "Courier New, monospace", fontSize: 9, textTransform: "uppercase", letterSpacing: 3, border: "1px solid #111", color: "#111", display: "inline-block", padding: "2px 8px", marginBottom: 10 },
  agentText: { fontSize: 13, lineHeight: 1.7, color: "#222", textAlign: "left" },
  verdictBox: { border: "3px solid #111", padding: "1.25rem", background: "#111", color: "#fff", marginTop: "1.5rem" },
  verdictLabel: { fontFamily: "Courier New, monospace", fontSize: 9, textTransform: "uppercase", letterSpacing: 3, color: "#888", marginBottom: 6 },
  verdictText: { fontSize: 15, lineHeight: 1.6, color: "#fff" },
};