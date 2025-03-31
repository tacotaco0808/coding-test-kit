import os
from pathlib import Path
from hashlib import sha256


input_path = Path("./input")
output_path = Path("./output")
output_path.mkdir(parents=True, exist_ok=True)
testcase_path = Path("./testcase")

TESTCASES_COUNT = len([_ for _ in testcase_path.glob("*.txt")])
result = {
    "OK": 0,
    "NG": 0,
}

for input_file in input_path.glob("*.txt"):
    output_file = output_path.joinpath(input_file.name)
    os.system(f"python main.py 0< {input_file.absolute()} > {output_file}")
    o = output_file.read_text()
    e = testcase_path.joinpath(input_file.name).read_text()
    if sha256(o.encode()).hexdigest() != sha256(e.encode()).hexdigest():
        print(output_file, "> NG")
        line_no = 1
        for o_line, e_line in zip(o.split("\n"), e.split("\n")):
            if o_line != e_line:
                print(
                    "===", output_file, "===",
                    "\nLineNo >", line_no,
                    "\nOutput >", o_line,
                    "\nExcept >", e_line
                )
        result["NG"] += 1
    else:
        result["OK"] += 1

print(
    "\n=== RESULT ===\n"
    f"TOTAL: {TESTCASES_COUNT}\n"
    f"OK   : {result['OK']}\n"
    f"NG   : {result['NG']}\n"
)
