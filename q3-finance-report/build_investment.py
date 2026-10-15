"""Investment summary deck (List of Investment FY25, date update 21 Sep 2026) in the finance report template."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import deckkit
from deckkit import *

OUT = sys.argv[1]
deckkit.SUBTITLE = "TGFB Group | List of Investment for All Companies | Updated 21 September 2026 | All figures in RM"
deckkit.BADGE = "FY25"
deckkit.SOURCE = "Source: List of Investment FY25 - Summary of Investment (date update 21 September 2026)"

# (type, amount, current value, remark) — TGFB holdings
HOLDINGS = [
    ("Unit Trust - AIIMAN",                      300000.00,  317424.29, "Valued as of 19/06/2026"),
    ("Maybank Malaysia Sukuk Fund",              677000.00,  681960.40, "Valued as of 19/06/2026"),
    ("Gold (1 kg)",                              472494.00,  610749.00, "Bought 19 May 2025"),
    ("Gold (1 kg)",                              618637.00,  610749.00, "Bought 20 Mar 2026; below cost"),
    ("Fixed Deposit - Loan Properties (FDR 1)",  140427.00,  140427.00, "Deducted from bank account as at 1 Jul 2026"),
    ("Fixed Deposit - Loan Properties (FDR 2)",   73425.00,   73425.00, "Deducted from bank account as at 1 Jul 2026"),
    ("Fixed Deposit - Loan Properties (FDR 3)",   72441.00,   72441.00, "Deducted from bank account as at 1 Jul 2026"),
    ("Fixed Deposit",                           2000000.00, 2000000.00, "Placed 3 Sep 2026, 1 year @ 3.3%, matures 3 Sep 2027"),
]
# (company, type, amount, current value, profit, remark) — matured, not renewed
OTHER_FD = [
    ("TGCK",   "Fixed Deposit (Maybank)", 0.0, 0.0, 33271.24, "Matured 19 Sep 2026, not renewed; accumulated profit on RM1M FD"),
    ("TGL",    "Fixed Deposit (Maybank)", 0.0, 0.0,   210.00, "12-month FD matured 17 Sep 2026, not renewed"),
    ("Bebeks", "Fixed Deposit (Maybank)", 0.0, 0.0,   210.00, "12-month FD matured 17 Sep 2026, not renewed"),
]
STATED_TOTAL = (4354424.00, 4507175.69, 152751.69)

amt = sum(h[1] for h in HOLDINGS); cur = sum(h[2] for h in HOLDINGS); gain = cur - amt
assert all(abs(a - b) < 0.005 for a, b in zip((amt, cur, gain), STATED_TOTAL)), (amt, cur, gain)
other_profit = sum(o[4] for o in OTHER_FD)

def group(pred):
    rows = [h for h in HOLDINGS if pred(h[0])]
    return sum(h[1] for h in rows), sum(h[2] for h in rows)
fd_a, fd_c = group(lambda n: n.startswith("Fixed Deposit"))
gold_a, gold_c = group(lambda n: n.startswith("Gold"))
fund_a, fund_c = group(lambda n: n.startswith(("Unit Trust", "Maybank")))
assert abs(fd_a + gold_a + fund_a - amt) < 0.005

def K(v): return f"RM{abs(v)/1e3:.1f}K"
def ret(a, c): return (c - a) / a if a else 0.0
def pct_cell(v, fill=PCT): return (f"{v:.1%}", fill, RED if v < -0.00005 else INK, True, C)
def amt_cells(vals, fills):
    return [(money(v), f, RED if v < -0.005 else INK, True, R) for v, f in zip(vals, fills)]

# ---------- Slide 1: Summary of Investment ----------
s = frame("Investment Portfolio: Summary of Investment",
          f"TGFB holds {M(amt)} of investments, now valued at {M(cur)}: an unrealised gain of {K(gain)} ({ret(amt, cur):.1%}), "
          f"driven mainly by the gold bought in May 2025 (+{K(HOLDINGS[2][2] - HOLDINGS[2][1])}).", 10.5)
cards = [
    ("TOTAL AMOUNT INVESTED", M(amt), INK, f"{len(HOLDINGS)} holdings, all under TGFB", GOLD),
    ("CURRENT VALUE", M(cur), INK, "As at 21 Sep 2026 update", ORANGE),
    ("UNREALISED PROFIT", K(gain), INK, f"+{ret(amt, cur):.1%} on amount invested", GREEN),
    ("FIXED DEPOSITS", M(fd_a), INK, f"{fd_a / amt:.1%} of amount invested", NAVY),
    ("MATURED FD PROFIT", K(other_profit), INK, "TGCK, TGL & Bebeks (not renewed)", GOLD),
]
cw, gap = 2.27, 0.355
for i, (lab, val, vc, sub, bar) in enumerate(cards):
    x = L + i * (cw + gap)
    rect(s, x, 1.6, cw, 0.78, WHITE, BORDER)
    rect(s, x, 1.6, 0.06, 0.78, bar)
    text(s, x + 0.14, 1.66, cw - 0.2, 0.16, [[(lab, False, MUTED, 6.5)]])
    text(s, x + 0.14, 1.8, cw - 0.2, 0.34, [[(val, True, vc, 17)]])
    text(s, x + 0.14, 2.15, cw - 0.2, 0.16, [[(sub, False, MUTED, 6)]])

section_bar(s, 2.56, "TGFB: List of Investment", h=0.26, size=10)
cols1 = [3.1, 1.5, 1.5, 1.45, 0.8, 4.42]
rows1 = []
for name, a, c, rem in HOLDINGS:
    rows1.append([(name, LGOLD, INK, True, Lf)] + amt_cells([a, c, c - a], [ALT, WHITE, ALT])
                 + [pct_cell(ret(a, c)), (rem, WHITE, INK, True, Lf)])
rows1.append([("TOTAL", NAVY, WHITE, True, Lf)] + amt_cells([amt, cur, gain], [GOLD] * 3)
             + [pct_cell(ret(amt, cur), GOLD), ("Unrealised gain on TGFB holdings", GOLD, INK, True, Lf)])
table(s, L, 2.82, cols1, [0.36] + [0.35] * len(rows1),
      ["Type of Investment", "Amount (RM)", "Current Value (RM)", "Profit / (Loss)", "Return", "Remarks"],
      rows1, size=10, header_size=10)
gold_gain = gold_c - gold_a
rect(s, L, 6.5, W, 0.48, WHITE, BORDER)
text(s, L + 0.12, 6.5, W - 0.24, 0.48,
     [[("KEY TAKEAWAY ", True, MUTED, 8),
       (f"Gold is the main source of gain (+{K(gold_gain)} net across both bars). The {M(2e6)} fixed deposit at 3.3% p.a. should earn about "
        f"{K(2e6 * 0.033)} by Sep 2027. Unit trust and sukuk values are as at 19 Jun 2026 and should be refreshed.", True, INK, 8)]],
     anchor=MSO_ANCHOR.MIDDLE)

# ---------- Slide 2: Allocation & group deposits ----------
s = frame("Investment Portfolio: Allocation & Group Deposits",
          f"Fixed deposits make up about half of the portfolio; gold gives the highest return at {ret(gold_a, gold_c):.1%}. "
          f"TGCK, TGL and Bebeks FDs matured in September and were not renewed.", 11)
section_bar(s, 1.5, "Allocation by Asset Class (TGFB)", h=0.26, size=10.5)
cols2 = [2.6, 1.5, 1.5, 1.4, 0.8, 1.05, 3.92]
alloc = [
    ("Fixed Deposits", fd_a, fd_c, "4 placements; returns not yet accrued in the list"),
    ("Gold", gold_a, gold_c, "2 x 1kg; 2025 bar +29.3%, 2026 bar -1.3%"),
    ("Unit Trust & Sukuk Funds", fund_a, fund_c, "AIIMAN +5.8%, Sukuk +0.7% (as of 19/06/2026)"),
]
rows2 = []
for name, a, c, rem in alloc:
    rows2.append([(name, LGOLD, INK, True, Lf)] + amt_cells([a, c, c - a], [ALT, WHITE, ALT])
                 + [pct_cell(ret(a, c)), pct_cell(c / cur), (rem, WHITE, INK, True, Lf)])
rows2.append([("TOTAL", NAVY, WHITE, True, Lf)] + amt_cells([amt, cur, gain], [GOLD] * 3)
             + [pct_cell(ret(amt, cur), GOLD), pct_cell(1.0, GOLD), ("", GOLD, INK, True, Lf)])
table(s, L, 1.76, cols2, [0.4] + [0.42] * len(rows2),
      ["Asset Class", "Amount (RM)", "Current Value (RM)", "Profit / (Loss)", "Return", "% of Portfolio", "Remarks"],
      rows2, size=10.5, header_size=10)

section_bar(s, 4.2, "Other Group Companies: Fixed Deposits", h=0.26, size=10.5)
cols3 = [1.3, 2.4, 1.5, 1.5, 1.4, 4.67]
rows3 = []
for co, typ, a, c, pr, rem in OTHER_FD:
    rows3.append([(co, LGOLD, INK, True, Lf), (typ, WHITE, INK, True, Lf)] + amt_cells([a, c, pr], [ALT, WHITE, ALT])
                 + [(rem, WHITE, INK, True, Lf)])
rows3.append([("TOTAL", NAVY, WHITE, True, Lf), ("", GOLD, INK, True, Lf)] + amt_cells([0, 0, other_profit], [GOLD] * 3)
             + [("Realised profit; not in the portfolio total above", GOLD, INK, True, Lf)])
table(s, L, 4.46, cols3, [0.38] + [0.38] * len(rows3),
      ["Company", "Type of Investment", "Amount (RM)", "Current Value (RM)", "Profit", "Remarks"],
      rows3, size=10, header_size=10)
rect(s, L, 6.5, W, 0.48, WHITE, BORDER)
text(s, L + 0.12, 6.5, W - 0.24, 0.48,
     [[("KEY TAKEAWAY ", True, MUTED, 8),
       (f"Total profit across all companies is {K(gain + other_profit)}: {K(gain)} unrealised on TGFB holdings plus {K(other_profit)} "
        "realised from matured FDs at TGCK, TGL and Bebeks. The list shows no remaining FD balance outside TGFB.", True, INK, 8)]],
     anchor=MSO_ANCHOR.MIDDLE)

prs.save(OUT)
print("saved", OUT, "| amt", amt, "cur", cur, "gain", round(gain, 2), "fd", fd_a, "gold", gold_a, gold_c, "funds", fund_a, round(fund_c, 2), "other", other_profit)
