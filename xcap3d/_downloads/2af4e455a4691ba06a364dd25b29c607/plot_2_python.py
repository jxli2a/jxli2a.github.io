"""
From Python
===========

The run of the command-line example from a script: one call, then the numbers
from the record. ``DB`` is the Green's-function database directory, provided
by the operator.
"""

# %%
from pathlib import Path

from xcap3d import Result, run_event

DB = Path("DB")
OUT = Path("xcap3d-out")

# %%
# The run
# -------
# ``run_event`` takes the options of ``xcap3d run``: it downloads the event
# from SCEDC, removes the instrument responses, inverts and writes
# ``result.json`` and, with ``write_report``, the report. It returns the record,
# a dictionary with the contents of ``result.json``; printing it gives the
# solution.
result = run_event("38695658", DB, out=OUT, mt="full", refine=True, write_report=True)
print(result)

# %%
# The numbers
# -----------
# The shortcuts cover the solution; everything else is in the dictionary:
# the depth scan, every station with its weights and fits, the QC record, the
# database release and the inputs with their checksums.
print(result.strike, result.dip, result.rake, result.depth, result.mw, result.vr)
print(
    result["solution"]["n_stations"], "stations,", result["solution"]["n_components"], "components"
)
nd = result["non_dc"]
print(f"ISO {nd['iso_pct']:.1f} %  CLVD {nd['clvd_pct']:.1f} %  DC {nd['dc_pct']:.1f} %")
for row in result["depth_scan"][:3]:
    print(row)

# %%
# A record on disk
# ----------------
# ``Result.from_file`` reads a ``result.json`` written earlier, by a script or
# by the command line.
again = Result.from_file(OUT / "38695658" / "result.json")
print(again)
