"""CL: date arithmetic for catalysts, and buyback headroom."""
import datetime as dt
TODAY = dt.date(2026, 11, 21)
# CL-105 remote-access IFR effective 2026-11-19 [F]; CL-106 licence within 90 days of effective date [F]
eff = dt.date(2026, 11, 19)
print(f"Remote-access IFR 90-day licence deadline: {eff + dt.timedelta(days=90)}")
# CL-099 buyback cap JPY 280bn / 11,000,000 shares, ends 2027-03-24 [F]; CL-100 progress to 31 Oct 2026 [F]
CAP_YEN, CAP_SH = 280_000_000_000, 11_000_000
DONE_YEN, DONE_SH = 14_563_326_000, 420_900
print(f"Buyback headroom after 31 Oct 2026: JPY {CAP_YEN-DONE_YEN:,} ; shares {CAP_SH-DONE_SH:,}")
print(f"Share of yen cap used by 31 Oct 2026: {DONE_YEN/CAP_YEN*100:.1f}%")
dated = {"Interim dividend payment (CL-093)": dt.date(2026, 12, 1),
         "BIS affiliates-rule stay ends (CL-104)": dt.date(2027, 1, 10),
         "BIS remote-access IFR comments due (CL-105)": dt.date(2027, 1, 19),
         "Remote-access 90-day licence deadline (computed)": eff + dt.timedelta(days=90),
         "Buyback period ends (CL-099)": dt.date(2027, 3, 24),
         "FY2026 / MTP3 end (CL-101)": dt.date(2027, 3, 31),
         "AGM voting-rights record date per 84th ASR p.58/p.199 and Share Information page (CL-133, CL-097)": dt.date(2027, 5, 15),
         "Teradyne at UBS Global Technology and AI Conference (CL-108)": dt.date(2026, 11, 30),
         "CB maturity (CL-103)": dt.date(2031, 3, 28)}
for k, d in dated.items():
    print(f"{d}  +{(d-TODAY).days} days  {k}")
# CL-111 full-year results dates (IR calendar) [F]: pattern only, FY2026 date not committed
for d in (dt.date(2025, 4, 25), dt.date(2026, 4, 27)):
    print(f"Past full-year results: {d} ({d.strftime('%a')})")
# CL-133 (84th ASR p.199) / CL-097: AGM within three months from the 15 May record date [F]; CL-096/CL-134 84th AGM 2026-07-31 [F]
# CL-095 IR calendar prints 31 Mar as the voting-rights record date: conflicts with CL-133/CL-134/CL-097
rec = dt.date(2027, 5, 15)
print(f"85th AGM window (record date + 3 months): {rec} to {rec.replace(month=8)}")
