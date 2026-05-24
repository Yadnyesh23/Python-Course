essential_subs = {"DSA", "DBMS" " ML"}
optional_subs = {"IOT", "Cyber Security", "DSA"}

all_subs = essential_subs | optional_subs
print(f"All subs : {all_subs}")

common_subs = essential_subs & optional_subs
print(f"Common subs : {common_subs}")

only_essential = essential_subs - optional_subs
print(f"Only essential subs : {only_essential}")

