# WAP_to_extract_all_the_uppercase_characters_present_in_string
s = 'pRogRAMmIng'
st = ''
for i in s:
    if "A" <= i <= "Z":
        st += i
print(st)