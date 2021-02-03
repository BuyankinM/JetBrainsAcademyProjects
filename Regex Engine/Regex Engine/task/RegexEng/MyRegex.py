def parse_rex(regs: str):
    l_rex = []
    for c in regs:
        if c in "?*+":
            l_rex[-1]["mod"] = c
        else:
            l_rex.append({"symbol": c, "mod": ""})

    return l_rex


def check_rex(regs: str, inps: str):

    clean_regs = regs.strip("^$")
    if not clean_regs:
        # empty string
        return True
    else:
        start_fix = regs[0] == "^"
        end_fix = regs[-1] == "$"
        reg_list = parse_rex(clean_regs)

        len_reg = len(reg_list)
        len_input = len(inps)

        result = True

        for inp_ind in range(len_input):
            stop = False

            inp_mod = 0
            reg_ind = 0

            while reg_ind < len_reg:
                symbol_reg = reg_list[reg_ind]["symbol"]
                mod_reg = reg_list[reg_ind]["mod"]

                if symbol_reg == inps[reg_ind + inp_mod] or symbol_reg == ".":
                    if mod_reg and mod_reg in "+*":
                        str_id = inps[reg_ind + inp_mod]
                        while True:
                            next_ind_inp = reg_ind + inp_mod + 1
                            if next_ind_inp < len_input \
                                    and (symbol_reg == inps[next_ind_inp] or symbol_reg == "."):
                                str_id += inps[next_ind_inp]
                                inp_mod += 1
                            else:
                                break
                else:
                    # may be bad
                    break

                reg_ind += 1

            if reg_ind == len_reg:
                break

            if stop:
                break

        return result


reg, inp = input().split("|")
print(check_rex(reg, inp))
