import sys 
import re
from itertools import tee, izip

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)

scriptnum = sys.argv[1]
EVENT = sys.argv[2]

#o = open(newfile,"w")
#f = open(sys.argv[1],'r')
qst_funcs = ['if','elseif','msg','dialog','gobind','break','summonitem','setflag','journal','lawpoints','chaospoints','removeitem','cleardebt','emote','msgnote','newbindpoint','}']
qst_vars = ['1-','flag','race','class','uclass','urace','deity']
f = open(str(scriptnum) + EVENT + ".tmp",'r')
g = open(str(scriptnum) + EVENT + ".tmp",'r')
outfile = open(str(scriptnum) + EVENT + ".out",'a')

brackets = 0
in_event = False
lines_read = 0
tabs = 0

uses_chance = False
uses_bchance = False
uses_cchance = False
uses_dchance = False
updates_script = False
updates_s0 = False
updates_s1 = False
updates_s2 = False
updates_s3 = False
updates_s4 = False
updates_s5 = False
updates_s6 = False
updates_s7 = False
updates_s8 = False
updates_s9 = False
up_script = False
up_s0 = False
up_s1 = False
up_s2 = False
up_s3 = False
up_s4 = False
up_s5 = False
up_s6 = False
up_s7 = False
up_s8 = False
up_s9 = False

for line in g:
	if "$chance" in line:
		uses_chance = True
	if "$bchance" in line:
		uses_bchance = True
	if "$cchance" in line:
		uses_cchance = True
	if "$dchance" in line:
		uses_dchance = True
	if "scriptstatus(" in line:
		up_script = True
	if "setsubstring(0" in line:
		up_s0 = True
	if "setsubstring(1" in line:
		up_s1 = True
	if "setsubstring(2" in line:
		up_s2 = True
	if "setsubstring(3" in line:
		up_s3 = True
	if "setsubstring(4" in line:
		up_s4 = True
	if "setsubstring(5" in line:
		up_s5 = True
	if "setsubstring(6" in line:
		up_s6 = True
	if "setsubstring(7" in line:
		up_s7 = True
	if "setsubstring(8" in line:
		up_s8 = True
	if "setsubstring(9" in line:
		up_s9 = True

g.close()
g = open(str(scriptnum) + EVENT + ".tmp",'r')

for line in g:		
	if up_script and "$script_status" in line:
		updates_script = True
	if up_s0 and "$substring(0" in line:
		updates_s0 = True
	if up_s0 and "$substring(1" in line:
		updates_s1 = True
	if up_s0 and "$substring(2" in line:
		updates_s2 = True
	if up_s0 and "$substring(3" in line:
		updates_s3 = True
	if up_s0 and "$substring(4" in line:
		updates_s4 = True
	if up_s0 and "$substring(5" in line:
		updates_s5 = True
	if up_s0 and "$substring(6" in line:
		updates_s6 = True
	if up_s0 and "$substring(7" in line:
		updates_s7 = True
	if up_s0 and "$substring(8" in line:
		updates_s8 = True
	if up_s0 and "$substring(9" in line:
		updates_s9 = True

g.close()

def do_vars(s):
	s = s.replace("&&","and")
	s = re.sub(r'\$1\- =~[^"]*(".*")', r'string.find(words,\1)', s)
	s = s.replace("$flag","other:GetFlag")
	s = re.sub(r'\$random\((\d+)\)', r'math.random(\1) - 1', s)
	if updates_s0:
		s = s.replace("$substring(0)","check_substring_0")
	if updates_s1:
		s = s.replace("$substring(1)","check_substring_1")
	if updates_s2:
		s = s.replace("$substring(2)","check_substring_2")
	if updates_s3:
		s = s.replace("$substring(3)","check_substring_3")
	if updates_s4:
		s = s.replace("$substring(4)","check_substring_4")
	if updates_s5:
		s = s.replace("$substring(5)","check_substring_5")
	if updates_s6:
		s = s.replace("$substring(6)","check_substring_6")
	if updates_s7:
		s = s.replace("$substring(7)","check_substring_7")
	if updates_s8:
		s = s.replace("$substring(8)","check_substring_8")
	if updates_s9:
		s = s.replace("$substring(9)","check_substring_9")
	s = s.replace("$substring(0)","substring_0")
	s = s.replace("$substring(1)","substring_1")
	s = s.replace("$substring(2)","substring_2")
	s = s.replace("$substring(3)","substring_3")
	s = s.replace("$substring(4)","substring_4")
	s = s.replace("$substring(5)","substring_5")
	s = s.replace("$substring(6)","substring_6")
	s = s.replace("$substring(7)","substring_7")
	s = s.replace("$substring(8)","substring_8")
	s = s.replace("$substring(9)","substring_9")
	s = s.replace("NULL","nil")
	s = s.replace("$ustat(MR)","other:GetStat(\"mr\")")
	s = s.replace("$ustat(FR)","other:GetStat(\"fr\")")
	s = s.replace("$ustat(CR)","other:GetStat(\"cr\")")
	s = s.replace("$ustat(PR)","other:GetStat(\"pr\")")
	s = s.replace("$ustat(DR)","other:GetStat(\"dr\")")
	s = s.replace("$urace","other:GetRace()")
	s = s.replace("$uclass","other:GetClass()")
	s = s.replace("$userid","other")
	s = s.replace("$spellid","spellid")
	s = s.replace("$race","other:GetRaceName()")
	s = s.replace("$faction","other:GetCon(self)")
	s = s.replace("$name","other:GetName()")
	s = s.replace("$mname","self:GetName()")
	s = s.replace("$ulevel","other:GetLevel()")
	s = s.replace("$zoneid","GetZoneID()")
	s = s.replace("$ssex","other:GetGender()")
	s = s.replace("$udist","self:GetDist(other)")
	s = s.replace("$npc_count","NPCCount")
	s = s.replace("$locx","other:GetX()")
	s = s.replace("$locy","other:GetY()")
	s = s.replace("$locz","other:GetZ()")
	s = s.replace("$npc_locx","self:GetX()")
	s = s.replace("$npc_locy","self:GetY()")
	s = s.replace("$npc_locz","self:GetZ()")
	s = s.replace("$global(","GetGlobal(")
	s = s.replace("$signal","signal")
	s = s.replace("$eventratio","self:GetHPTrigger()")
	s = s.replace("$hpratio","self:GetStat(\"hpratio\")")
	if updates_script:
		s = s.replace("$script_status","check_script_status")
	s = s.replace("$script_status","script_status")
	s = s.replace("$primarytarget","primarytarget(self)")
	s = s.replace("$randtarget","randtarget(self)")
	s = s.replace("$auxtarget","auxtarget(self)")
	s = s.replace("$highestdamage","highestdamage(self)")
	s = s.replace("$lowesttarget","lowesttarget(self)")
	s = s.replace("$ramptarget","ramptarget(self)")
	s = s.replace("$meleetarget","meleetarget(self)")
	s = s.replace("$auxmeleetarget","auxmeleetarget(self)")
	s = s.replace("$fartarget","fartarget(self)")
	s = s.replace("$lostarget","lostarget(self)")
	s = s.replace("$nolostarget","nolostarget(self)")
	s = s.replace("$getdmghate","getdmghate(self)")
	s = s.replace("$hatesizetotal","hatesizetotal(self)")
	s = s.replace("$hatesizeclients","hatesizeclients(self)")
	s = s.replace("$npccorpse_count(","npccorpse_count(")
	s = s.replace("$clientcount","clientcount(self)")
	s = s.replace("$itemcount","items_table")
	s = s.replace("$hasitem(","HasItem(other,")
	s = s.replace("$casting == 0","not self:IsCasting()")
	s = s.replace("$battle == 0","not self:InCombat()")
	s = s.replace("$casting == 1","self:IsCasting()")
	s = s.replace("$battle == 1","self:InCombat()")
	s = s.replace("$combatrange == 1","self:InCombatRange(other)")
	s = s.replace("$combatrange == 0","not self:InCombatRange(other)")
	s = s.replace("$fighting == 0","not self:InCombat()")
	s = s.replace("$fighting == 1","self:InCombat()")
	s = re.sub(r'\$buffID\((\d+)\) == 1', r'HasBuff(other,\1)', s)
	s = re.sub(r'\$buffID\((\d+)\) == 0', r'not HasBuff(other,\1)', s)
	return s
	
def do_msg_vars(s):
	s = s.replace("$ustat(MR)","other:GetStat(\"mr\")")
	s = s.replace("$ustat(FR)","other:GetStat(\"fr\")")
	s = s.replace("$ustat(CR)","other:GetStat(\"cr\")")
	s = s.replace("$ustat(PR)","other:GetStat(\"pr\")")
	s = s.replace("$ustat(DR)","other:GetStat(\"dr\")")
	s = s.replace("$substring(0)","substring_0")
	s = s.replace("$substring(1)","substring_1")
	s = s.replace("$substring(2)","substring_2")
	s = s.replace("$substring(3)","substring_3")
	s = s.replace("$substring(4)","substring_4")
	s = s.replace("$substring(5)","substring_5")
	s = s.replace("$substring(6)","substring_6")
	s = s.replace("$substring(7)","substring_7")
	s = s.replace("$substring(8)","substring_8")
	s = s.replace("$substring(9)","substring_9")
	s = re.sub(r'\$calc\((.+)\)', r'" .. \1 .. "', s)
	s = re.sub(r'\$flag\((\d+)\)', r'" .. other:GetFlag(\1) .. "', s)
	s = s.replace("$sex ","\" .. sex() .. \"")
	s = s.replace("$sex2","\" .. sex2() .. \"")
	s = s.replace("$sex3","\" .. sex3() .. \"")
	s = s.replace("$sex4","\" .. sex4() .. \"")
	s = s.replace("$race","\" .. other:GetRaceName() .. \"")
	s = s.replace("$name","\" .. other:GetName() .. \"")
	s = s.replace("$ulevel","\" .. other:GetLevel() .. \"")
	s = s.replace("$mname","\" .. self:GetName() .. \"")
	s = s.replace("$class","\" .. other:GetClassName() .. \"")
	return s

def do_msg_calcs(s):
	calcs_done = False
	changes = 0
	while not calcs_done:
		if "$calc" not in s:
			calcs_done = True
		else:
			calc_extract_start = s.find("$calc")
			parens = 0
			started = False
			offset = 0
			for x in s[calc_extract_start:]:
				offset = offset + 1
				if x == "(" and not started:
					parens = parens + 1
					started = True
				elif x == "(":
					parens = parens + 1
				elif x == ")" and parens > 1:
					parens = parens - 1
				elif x == ")":
					break
				
			calc_string = s[calc_extract_start:calc_extract_start + offset]
			if changes == 0:
				s = s.replace(calc_string, "\" .. (" + calc_string[6:offset-1] + ") .. \"")
			else:
				s = s.replace(calc_string, calc_string[6:offset-1])
			changes = changes + 1
			s = s.replace("$flag","other:GetFlag")
			s = re.sub(r'\$ustat\((\w+)\) == 1', r'other:GetStat(\1)', s)
			s = s.replace("$npc_count","NPCCount")
	return s

def do_calcs(s):
	calcs_done = False
	changes = 0
	while not calcs_done:
		if "$calc" not in s:
			calcs_done = True
		else:
			calc_extract_start = s.find("$calc")
			parens = 0
			started = False
			offset = 0
			for x in s[calc_extract_start:]:
				offset = offset + 1
				if x == "(" and not started:
					parens = parens + 1
					started = True
				elif x == "(":
					parens = parens + 1
				elif x == ")" and parens > 1:
					parens = parens - 1
				elif x == ")":
					break
				
			calc_string = s[calc_extract_start:calc_extract_start + offset]
			s = s.replace(calc_string, "(" + calc_string[6:offset-1] + ")")
			changes = changes + 1
			s = re.sub(r'\$random\((\d+)\)', r'math.random(\1) - 1', s)
			s = s.replace("$flag","other:GetFlag")
			s = s.replace("$ustat(MR)","other:GetStat(\"mr\")")
			s = s.replace("$ustat(FR)","other:GetStat(\"fr\")")
			s = s.replace("$ustat(CR)","other:GetStat(\"cr\")")
			s = s.replace("$ustat(PR)","other:GetStat(\"pr\")")
			s = s.replace("$ustat(DR)","other:GetStat(\"dr\")")
			s = s.replace("$npc_count","NPCCount")
	return s



for line, next_line in pairwise(f):
	if not in_event and brackets < 1:
		if re.search(r'^EVENT_SPAWN',line):
			in_event = True
			outfile.write("function EVENT_SPAWN(self)" + "\n")
			tabs = tabs + 1
		elif re.search(r'^EVENT_SAY',line):
			in_event = True
			outfile.write("function EVENT_SAY(self, other, words)" + "\n")
			if updates_script:
				outfile.write("\t" + "check_script_status = script_status" + "\n")
			if updates_s0:
				outfile.write("\t" + "check_substring_0 = substring_0" + "\n")
			if updates_s1:
				outfile.write("\t" + "check_substring_1 = substring_1" + "\n")
			if updates_s2:
				outfile.write("\t" + "check_substring_2 = substring_2" + "\n")
			if updates_s3:
				outfile.write("\t" + "check_substring_3 = substring_3" + "\n")
			if updates_s4:
				outfile.write("\t" + "check_substring_4 = substring_4" + "\n")
			if updates_s5:
				outfile.write("\t" + "check_substring_5 = substring_5" + "\n")
			if updates_s6:
				outfile.write("\t" + "check_substring_6 = substring_6" + "\n")
			if updates_s7:
				outfile.write("\t" + "check_substring_7 = substring_7" + "\n")
			if updates_s8:
				outfile.write("\t" + "check_substring_8 = substring_8" + "\n")
			if updates_s9:
				outfile.write("\t" + "check_substring_9 = substring_9" + "\n")
			outfile.write("if not self:InCombat() then" + "\n")
			tabs = tabs + 1
		elif re.search(r'^EVENT_AGGROSAY',line):
			in_event = True
			outfile.write("function EVENT_AGGROSAY(self, other)" + "\n")
			if updates_script:
				outfile.write("\t" + "check_script_status = script_status" + "\n")
			if updates_s0:
				outfile.write("\t" + "check_substring_0 = substring_0" + "\n")
			if updates_s1:
				outfile.write("\t" + "check_substring_1 = substring_1" + "\n")
			if updates_s2:
				outfile.write("\t" + "check_substring_2 = substring_2" + "\n")
			if updates_s3:
				outfile.write("\t" + "check_substring_3 = substring_3" + "\n")
			if updates_s4:
				outfile.write("\t" + "check_substring_4 = substring_4" + "\n")
			if updates_s5:
				outfile.write("\t" + "check_substring_5 = substring_5" + "\n")
			if updates_s6:
				outfile.write("\t" + "check_substring_6 = substring_6" + "\n")
			if updates_s7:
				outfile.write("\t" + "check_substring_7 = substring_7" + "\n")
			if updates_s8:
				outfile.write("\t" + "check_substring_8 = substring_8" + "\n")
			if updates_s9:
				outfile.write("\t" + "check_substring_9 = substring_9" + "\n")
			outfile.write("if self:InCombat() then" + "\n")
			tabs = tabs + 1
		elif re.search(r'^EVENT_ITEM',line):
			in_event = True
			outfile.write("function EVENT_ITEM(self, other, items_table)" + "\n")
			if updates_script:
				outfile.write("\t" + "check_script_status = script_status" + "\n")
			if updates_s0:
				outfile.write("\t" + "check_substring_0 = substring_0" + "\n")
			if updates_s1:
				outfile.write("\t" + "check_substring_1 = substring_1" + "\n")
			if updates_s2:
				outfile.write("\t" + "check_substring_2 = substring_2" + "\n")
			if updates_s3:
				outfile.write("\t" + "check_substring_3 = substring_3" + "\n")
			if updates_s4:
				outfile.write("\t" + "check_substring_4 = substring_4" + "\n")
			if updates_s5:
				outfile.write("\t" + "check_substring_5 = substring_5" + "\n")
			if updates_s6:
				outfile.write("\t" + "check_substring_6 = substring_6" + "\n")
			if updates_s7:
				outfile.write("\t" + "check_substring_7 = substring_7" + "\n")
			if updates_s8:
				outfile.write("\t" + "check_substring_8 = substring_8" + "\n")
			if updates_s9:
				outfile.write("\t" + "check_substring_9 = substring_9" + "\n")
			tabs = tabs + 1
		elif re.search(r'^EVENT_SCRIPT',line):
			in_event = True
			outfile.write("function EVENT_TIMER(self, timer_id)" + "\n")
			tabs = tabs + 1
			outfile.write("\t" + "if timer_id == \"script\" then" + "\n")
			if updates_script:
				outfile.write("\t" + "check_script_status = script_status" + "\n")
			if updates_s0:
				outfile.write("\t" + "check_substring_0 = substring_0" + "\n")
			if updates_s1:
				outfile.write("\t" + "check_substring_1 = substring_1" + "\n")
			if updates_s2:
				outfile.write("\t" + "check_substring_2 = substring_2" + "\n")
			if updates_s3:
				outfile.write("\t" + "check_substring_3 = substring_3" + "\n")
			if updates_s4:
				outfile.write("\t" + "check_substring_4 = substring_4" + "\n")
			if updates_s5:
				outfile.write("\t" + "check_substring_5 = substring_5" + "\n")
			if updates_s6:
				outfile.write("\t" + "check_substring_6 = substring_6" + "\n")
			if updates_s7:
				outfile.write("\t" + "check_substring_7 = substring_7" + "\n")
			if updates_s8:
				outfile.write("\t" + "check_substring_8 = substring_8" + "\n")
			if updates_s9:
				outfile.write("\t" + "check_substring_9 = substring_9" + "\n")
			tabs = tabs + 1
		elif re.search(r'^EVENT_TRIGGERALL',line):
			in_event = True
			outfile.write("function EVENT_TIMER(self, timer_id)" + "\n")
			tabs = tabs + 1
			outfile.write("\t" * tabs + "if timer_id == \"triggerall\" then" + "\n")
			if updates_script:
				outfile.write("\t" + "check_script_status = script_status" + "\n")
			if updates_s0:
				outfile.write("\t" + "check_substring_0 = substring_0" + "\n")
			if updates_s1:
				outfile.write("\t" + "check_substring_1 = substring_1" + "\n")
			if updates_s2:
				outfile.write("\t" + "check_substring_2 = substring_2" + "\n")
			if updates_s3:
				outfile.write("\t" + "check_substring_3 = substring_3" + "\n")
			if updates_s4:
				outfile.write("\t" + "check_substring_4 = substring_4" + "\n")
			if updates_s5:
				outfile.write("\t" + "check_substring_5 = substring_5" + "\n")
			if updates_s6:
				outfile.write("\t" + "check_substring_6 = substring_6" + "\n")
			if updates_s7:
				outfile.write("\t" + "check_substring_7 = substring_7" + "\n")
			if updates_s8:
				outfile.write("\t" + "check_substring_8 = substring_8" + "\n")
			if updates_s9:
				outfile.write("\t" + "check_substring_9 = substring_9" + "\n")
			outfile.write("\t" * tabs + "op_success = 0" + "\n")
			outfile.write("\t" * tabs + "iter = 0" + "\n")
			outfile.write("\t" * tabs + "hate = self:GetHateList(\"entity\")" + "\n")
			outfile.write("\t" * tabs + "for k,other in pairs(hate) do" + "\n")
			outfile.write("\t" * tabs + "iter = iter + 1" + "\n")
			outfile.write("\t" * tabs + "if iter == #hate then op_success = 1" + "\n")
			tabs = tabs + 1
		elif re.search(r'^EVENT_SIGNAL',line):
			in_event = True
			outfile.write("function EVENT_SIGNAL(self, other, signal)" + "\n")
			if updates_script:
				outfile.write("\t" + "check_script_status = script_status" + "\n")
			if updates_s0:
				outfile.write("\t" + "check_substring_0 = substring_0" + "\n")
			if updates_s1:
				outfile.write("\t" + "check_substring_1 = substring_1" + "\n")
			if updates_s2:
				outfile.write("\t" + "check_substring_2 = substring_2" + "\n")
			if updates_s3:
				outfile.write("\t" + "check_substring_3 = substring_3" + "\n")
			if updates_s4:
				outfile.write("\t" + "check_substring_4 = substring_4" + "\n")
			if updates_s5:
				outfile.write("\t" + "check_substring_5 = substring_5" + "\n")
			if updates_s6:
				outfile.write("\t" + "check_substring_6 = substring_6" + "\n")
			if updates_s7:
				outfile.write("\t" + "check_substring_7 = substring_7" + "\n")
			if updates_s8:
				outfile.write("\t" + "check_substring_8 = substring_8" + "\n")
			if updates_s9:
				outfile.write("\t" + "check_substring_9 = substring_9" + "\n")
			tabs = tabs + 1
		elif re.search(r'^EVENT_COMBATEND',line):
			in_event = True
			outfile.write("function EVENT_COMBATEND(self)" + "\n")
			if updates_script:
				outfile.write("\t" + "check_script_status = script_status" + "\n")
			if updates_s0:
				outfile.write("\t" + "check_substring_0 = substring_0" + "\n")
			if updates_s1:
				outfile.write("\t" + "check_substring_1 = substring_1" + "\n")
			if updates_s2:
				outfile.write("\t" + "check_substring_2 = substring_2" + "\n")
			if updates_s3:
				outfile.write("\t" + "check_substring_3 = substring_3" + "\n")
			if updates_s4:
				outfile.write("\t" + "check_substring_4 = substring_4" + "\n")
			if updates_s5:
				outfile.write("\t" + "check_substring_5 = substring_5" + "\n")
			if updates_s6:
				outfile.write("\t" + "check_substring_6 = substring_6" + "\n")
			if updates_s7:
				outfile.write("\t" + "check_substring_7 = substring_7" + "\n")
			if updates_s8:
				outfile.write("\t" + "check_substring_8 = substring_8" + "\n")
			if updates_s9:
				outfile.write("\t" + "check_substring_9 = substring_9" + "\n")
			tabs = tabs + 1
		elif re.search(r'^EVENT_HP',line):
			in_event = True
			outfile.write("function EVENT_HP(self, other, damage)" + "\n")
			if updates_script:
				outfile.write("\t" + "check_script_status = script_status" + "\n")
			if updates_s0:
				outfile.write("\t" + "check_substring_0 = substring_0" + "\n")
			if updates_s1:
				outfile.write("\t" + "check_substring_1 = substring_1" + "\n")
			if updates_s2:
				outfile.write("\t" + "check_substring_2 = substring_2" + "\n")
			if updates_s3:
				outfile.write("\t" + "check_substring_3 = substring_3" + "\n")
			if updates_s4:
				outfile.write("\t" + "check_substring_4 = substring_4" + "\n")
			if updates_s5:
				outfile.write("\t" + "check_substring_5 = substring_5" + "\n")
			if updates_s6:
				outfile.write("\t" + "check_substring_6 = substring_6" + "\n")
			if updates_s7:
				outfile.write("\t" + "check_substring_7 = substring_7" + "\n")
			if updates_s8:
				outfile.write("\t" + "check_substring_8 = substring_8" + "\n")
			if updates_s9:
				outfile.write("\t" + "check_substring_9 = substring_9" + "\n")
			tabs = tabs + 1
		elif re.search(r'^EVENT_ATTACK',line):
			in_event = True
			outfile.write("function EVENT_ATTACK(self, other)" + "\n")
			if updates_script:
				outfile.write("\t" + "check_script_status = script_status" + "\n")
			if updates_s0:
				outfile.write("\t" + "check_substring_0 = substring_0" + "\n")
			if updates_s1:
				outfile.write("\t" + "check_substring_1 = substring_1" + "\n")
			if updates_s2:
				outfile.write("\t" + "check_substring_2 = substring_2" + "\n")
			if updates_s3:
				outfile.write("\t" + "check_substring_3 = substring_3" + "\n")
			if updates_s4:
				outfile.write("\t" + "check_substring_4 = substring_4" + "\n")
			if updates_s5:
				outfile.write("\t" + "check_substring_5 = substring_5" + "\n")
			if updates_s6:
				outfile.write("\t" + "check_substring_6 = substring_6" + "\n")
			if updates_s7:
				outfile.write("\t" + "check_substring_7 = substring_7" + "\n")
			if updates_s8:
				outfile.write("\t" + "check_substring_8 = substring_8" + "\n")
			if updates_s9:
				outfile.write("\t" + "check_substring_9 = substring_9" + "\n")
			tabs = tabs + 1
		elif re.search(r'^EVENT_DEATH',line):
			in_event = True
			outfile.write("function EVENT_DEATH(self, other, damage, killed_by_DoT)" + "\n")
			if updates_script:
				outfile.write("\t" + "check_script_status = script_status" + "\n")
			if updates_s0:
				outfile.write("\t" + "check_substring_0 = substring_0" + "\n")
			if updates_s1:
				outfile.write("\t" + "check_substring_1 = substring_1" + "\n")
			if updates_s2:
				outfile.write("\t" + "check_substring_2 = substring_2" + "\n")
			if updates_s3:
				outfile.write("\t" + "check_substring_3 = substring_3" + "\n")
			if updates_s4:
				outfile.write("\t" + "check_substring_4 = substring_4" + "\n")
			if updates_s5:
				outfile.write("\t" + "check_substring_5 = substring_5" + "\n")
			if updates_s6:
				outfile.write("\t" + "check_substring_6 = substring_6" + "\n")
			if updates_s7:
				outfile.write("\t" + "check_substring_7 = substring_7" + "\n")
			if updates_s8:
				outfile.write("\t" + "check_substring_8 = substring_8" + "\n")
			if updates_s9:
				outfile.write("\t" + "check_substring_9 = substring_9" + "\n")
			tabs = tabs + 1
		elif re.search(r'^EVENT_SLAY',line):
			in_event = True
			outfile.write("function EVENT_SLAY(self, other)" + "\n")
			if updates_script:
				outfile.write("\t" + "check_script_status = script_status" + "\n")
			if updates_s0:
				outfile.write("\t" + "check_substring_0 = substring_0" + "\n")
			if updates_s1:
				outfile.write("\t" + "check_substring_1 = substring_1" + "\n")
			if updates_s2:
				outfile.write("\t" + "check_substring_2 = substring_2" + "\n")
			if updates_s3:
				outfile.write("\t" + "check_substring_3 = substring_3" + "\n")
			if updates_s4:
				outfile.write("\t" + "check_substring_4 = substring_4" + "\n")
			if updates_s5:
				outfile.write("\t" + "check_substring_5 = substring_5" + "\n")
			if updates_s6:
				outfile.write("\t" + "check_substring_6 = substring_6" + "\n")
			if updates_s7:
				outfile.write("\t" + "check_substring_7 = substring_7" + "\n")
			if updates_s8:
				outfile.write("\t" + "check_substring_8 = substring_8" + "\n")
			if updates_s9:
				outfile.write("\t" + "check_substring_9 = substring_9" + "\n")
			tabs = tabs + 1
		elif re.search(r'^EVENT_SPELL',line):
			in_event = True
			outfile.write("function EVENT_SPELL(self, other, spellname, spellid, element, mana_used)" + "\n")
			if updates_script:
				outfile.write("\t" + "check_script_status = script_status" + "\n")
			if updates_s0:
				outfile.write("\t" + "check_substring_0 = substring_0" + "\n")
			if updates_s1:
				outfile.write("\t" + "check_substring_1 = substring_1" + "\n")
			if updates_s2:
				outfile.write("\t" + "check_substring_2 = substring_2" + "\n")
			if updates_s3:
				outfile.write("\t" + "check_substring_3 = substring_3" + "\n")
			if updates_s4:
				outfile.write("\t" + "check_substring_4 = substring_4" + "\n")
			if updates_s5:
				outfile.write("\t" + "check_substring_5 = substring_5" + "\n")
			if updates_s6:
				outfile.write("\t" + "check_substring_6 = substring_6" + "\n")
			if updates_s7:
				outfile.write("\t" + "check_substring_7 = substring_7" + "\n")
			if updates_s8:
				outfile.write("\t" + "check_substring_8 = substring_8" + "\n")
			if updates_s9:
				outfile.write("\t" + "check_substring_9 = substring_9" + "\n")
			tabs = tabs + 1
		if uses_chance:
			outfile.write("\t" * tabs)
			outfile.write("chance = math.random(100) - 1" + "\n")
		if uses_bchance:
			outfile.write("\t" * tabs)
			outfile.write("bchance = math.random(100) - 1" + "\n")
		if uses_cchance:
			outfile.write("\t" * tabs)
			outfile.write("cchance = math.random(100) - 1" + "\n")
		if uses_dchance:
			outfile.write("\t" * tabs)
			outfile.write("dchance = math.random(100) - 1" + "\n")
	else:
		f = line[:int(line.find("("))]
		if "if" not in f and "}" not in f:
			filler = line[int(line.find("(")) + 1:int(line.find(");"))]
			if f == "msgtext":
				outfile.write("\t" * tabs)
				filler = do_msg_vars(filler)
				outfile.write("self:text(\"" + filler + "\",other)" + "\n")
			if f == "msg":
				outfile.write("\t" * tabs)
				filler = do_msg_vars(filler)
				outfile.write("self:text(self:GetName() .. \" tells you, '" + filler + "'\",other)" + "\n")
			elif f == "emote":
				outfile.write("\t" * tabs)
				filler = do_msg_vars(filler)
				outfile.write("self:text(self:GetName() .. \" " + filler + "\",other)" + "\n")
			elif f == "text":
				outfile.write("\t" * tabs)
				filler = do_msg_vars(filler)
				outfile.write("self:text(\"" + filler + "\")" + "\n")
			elif f == "say":
				outfile.write("\t" * tabs)
				filler = do_msg_vars(filler)
				outfile.write("self:text(self:GetName() .. \" says, '" + filler + "'\")" + "\n")
			elif f == "shout":
				outfile.write("\t" * tabs)
				filler = do_msg_vars(filler)
				outfile.write("zonetext(self:GetName() .. \" shouts, '" + filler + "'\")" + "\n")
			elif f == "msgnote":
				outfile.write("\t" * tabs)
				filler = do_msg_vars(filler)
				outfile.write("self:text(\"NOTE: " + filler + "\",other,15)" + "\n")
			elif f == "dialog":
				outfile.write("\t" * tabs)
				filler = do_msg_vars(filler)
				outfile.write("other:dialog(self,\"" + filler + "\")" + "\n")
			elif f == "break":
				outfile.write("\t" * tabs)
				outfile.write("return" + "\n")
			elif f == "summonitem":
				item_id = filler[:int(filler.find(","))]
				amt = int(filler[int(filler.find(","))+1:])
				outfile.write("\t" * tabs)
				if amt > 0:
					outfile.write("other:giveitem(" + filler + ")" + "\n")
				else:
					outfile.write("other:giveitem(" + item_id + ")" + "\n")
			elif f == "exp":
				outfile.write("\t" * tabs)
				outfile.write("other:exp(" + filler + ")" + "\n")
			elif f == "signal":
				npc_id = filler[:int(filler.find(","))]
				val = filler[int(filler.find(","))+1:]
				outfile.write("\t" * tabs)
				outfile.write("signal(" + npc_id + "," + val + ",self)" + "\n")
			elif f == "setglobal":
				outfile.write("\t" * tabs)
				outfile.write("setglobal(" + filler + ")" + "\n")
			elif f == "repopspawn":
				outfile.write("\t" * tabs)
				outfile.write("respawn(" + filler + ")" + "\n")
			elif f == "scriptstatus":
				outfile.write("\t" * tabs)
				if filler == "-1":
					outfile.write("script_status = script_status + 1" + "\n")
				else:
					filler = do_calcs(filler)
					filler = do_vars(filler)
					outfile.write("script_status = " + filler + "\n")
			elif f == "startscript":
				outfile.write("\t" * tabs)
				outfile.write("self:timer(\"script\"," + filler + ")" + "\n")
			elif f == "pulltrigger":
				outfile.write("\t" * tabs)
				outfile.write("self:timer(\"triggerall\"," + filler + ")" + "\n")
			elif f == "doanim":
				outfile.write("\t" * tabs)
				outfile.write("self:doanim(" + filler + ")" + "\n")
			elif f == "setanim":
				outfile.write("\t" * tabs)
				outfile.write("self:setanim(" + filler + ")" + "\n")
			elif f == "setrace":
				outfile.write("\t" * tabs)
				outfile.write("self:setappearance(" + filler + ")" + "\n")
			elif f == "wipehate":
				outfile.write("\t" * tabs)
				outfile.write("self:wipehate()" + "\n")
			elif f == "depop":
				if int(filler) == 0:
					outfile.write("\t" * tabs)
					outfile.write("self:depop()" + "\n")
				else:
					outfile.write("\t" * tabs)
					outfile.write("depop(" + filler + ")" + "\n")
			elif f == "takecash":
				outfile.write("\t" * tabs)
				outfile.write("other:takecash(" + filler + ")" + "\n")
			elif f == "customnuke":
				filler = do_calcs(filler)
				filler = do_vars(filler)
				vars = filler.split(",")
				name = vars[0]
				damage = vars[1]
				element = vars[2]
				resist_adjust = vars[3]
				range = vars[4]
				secondary_spell = vars[5]
				tertiary_spell = vars[6]
				message = vars[7]
				target = vars[8]
				outfile.write("\t" * tabs)
				if target == "0":
					target = "other"
				outfile.write("self:customnuke(" + target + "," + name + "," + damage + "," + element + "," + resist_adjust + "," + message + "," + secondary_spell + "," + tertiary_spell + ")" + "\n")
			elif f == "customspell":
				filler = do_calcs(filler)
				filler = do_vars(filler)
				vars = filler.split(",")
				name = vars[0]
				damage = vars[1]
				element = vars[2]
				resist_adjust = vars[3]
				range = vars[4]
				secondary_spell = vars[5]
				tertiary_spell = vars[6]
				message = vars[7]
				coneVal = vars[8]
				losVal = vars[9]
				target = vars[10]
				if target == "0":
					target = "self"
				if int(coneVal) == 1:
					s_cone = ""
				elif int(coneVal) == 2:
					s_cone = "and not self:IsBehind(v) "
				elif int(coneVal) == 0:
					s_cone = "and self:IsBehind(v) "
				if int(losVal) == 1:
					s_los = ""
				elif int(coneVal) == 2:
					s_los = "and self:InLos(v) "
				elif int(coneVal) == 0:
					s_los = "and not self:InLos(v) "
				outfile.write("\t" * tabs)
				outfile.write("local hl = self:GetHateList(\"entity\")" + "\n")
				outfile.write("\t" * tabs)
				outfile.write("for k,v in pairs(hl) do" + "\n")
				tabs = tabs + 1
				outfile.write("\t" * tabs)
				outfile.write("if " + target + ":GetDist(v) <= " + range + s_cone + s_los + " then" + "\n")
				tabs = tabs + 1
				outfile.write("\t" * tabs)
				outfile.write("self:customnuke(v," + name + "," + damage + "," + element + "," + resist_adjust + "," + message + "," + secondary_spell + "," + tertiary_spell + ")" + "\n")
				tabs = tabs - 1
				outfile.write("\t" * tabs)
				outfile.write("end" + "\n")
				tabs = tabs - 1
				outfile.write("\t" * tabs)
				outfile.write("end" + "\n")
			elif f == "castspell":
				filler = do_vars(filler)
				spell_id = filler[:int(filler.find(","))]
				target = filler[int(filler.find(","))+1:]
				outfile.write("\t" * tabs)
				if target == "0":
					outfile.write("self:castspell(" + spell_id + ",other)" + "\n")
				else:
					outfile.write("self:castspell(" + spell_id + "," + target + ")" + "\n")
			elif f == "movegrp":
				vars = filler.split(",")
				zone = "\"" + vars[0] + "\", "
				x = vars[1] + ", "
				y = vars[2] + ", "
				z = vars[3]
				filler = zone + x + y + z
				outfile.write("\t" * tabs)
				outfile.write("if not other:InGroup() then" + "\n")
				tabs = tabs + 1
				outfile.write("\t" * tabs)
				outfile.write("other:zone(" + filler + ")" + "\n")
				tabs = tabs - 1
				outfile.write("\t" * tabs)
				outfile.write("else" + "\n")
				tabs = tabs + 1
				outfile.write("\t" * tabs)
				outfile.write("gl = other:GetGroup(\"entity\")" + "\n")
				outfile.write("\t" * tabs)
				outfile.write("for k,v in pairs(gl) do" + "\n")
				tabs = tabs + 1
				outfile.write("\t" * tabs)
				outfile.write("other:zone(" + filler + ")" + "\n")
				tabs = tabs - 1
				outfile.write("\t" * tabs)
				outfile.write("end" + "\n")
				tabs = tabs - 1
				outfile.write("\t" * tabs)
				outfile.write("end" + "\n")
			elif f == "faction":
				outfile.write("\t" * tabs)
				outfile.write("other:faction(" + filler + ")" + "\n")
			elif f == "setflag":
				outfile.write("\t" * tabs)
				outfile.write("other:setflag(" + filler + ")" + "\n")
			elif f == "journal":
				outfile.write("\t" * tabs)
				outfile.write("other:journal(" + filler + ")" + "\n")
			elif f == "lawpoints":
				outfile.write("\t" * tabs)
				outfile.write("other:setflag(4998, other:GetFlag(4998) + " + filler + ")" + "\n")
			elif f == "hptrigger":
				outfile.write("\t" * tabs)
				outfile.write("self:hptrigger(" + filler + ")" + "\n")
			elif f == "invul":
				outfile.write("\t" * tabs)
				if filler == "1":
					outfile.write("self:invul(true)" + "\n")
				elif filler == "0":
					outfile.write("self:invul(false)" + "\n")
				else:
					outfile.write("-- bad invul: " + filler + "\n")
			elif f == "uninvul":
				outfile.write("\t" * tabs)
				if filler == "0":
					outfile.write("self:invul(false)" + "\n")
				else:
					check_id = filler
					outfile.write("nl = GetNPCList()" + "\n")
					outfile.write("\t" * tabs)
					outfile.write("for k,v in pairs(nl) do" + "\n")
					tabs = tabs + 1
					outfile.write("\t" * tabs)
					outfile.write("if v:GetNPCID() == " + filler + "then" + "\n")
					tabs = tabs + 1
					outfile.write("\t" * tabs)
					outfile.write("v:invul(false)" + "\n")
					tabs = tabs - 1
					outfile.write("\t" * tabs)
					outfile.write("end" + "\n")
					tabs = tabs - 1
					outfile.write("\t" * tabs)
					outfile.write("end" + "\n")
			elif f == "increaseflag":
				filler = do_calcs(filler)
				filler = do_vars(filler)
				flag_id = filler[:int(filler.find(","))]
				amt = int(filler[int(filler.find(","))+1:])
				outfile.write("\t" * tabs)
				outfile.write("other:setflag(" + str(flag_id) + ", other:GetFlag(" + str(flag_id) +") + (" + str(amt) + "))" + "\n")
			elif f == "setsubstring":
				filler = do_calcs(filler)
				filler = do_vars(filler)
				substring_id = filler[:int(filler.find(","))]
				val = filler[int(filler.find(","))+1:]
				outfile.write("\t" * tabs)
				outfile.write("substring_" + substring_id + " = " + val + "\n")
			elif f == "clearsubstring":
				filler = do_calcs(filler)
				filler = do_vars(filler)
				outfile.write("\t" * tabs)
				outfile.write("substring_" + filler + " = nil" + "\n")
			elif f == "set":
				filler = do_calcs(filler)
				filler = do_vars(filler)
				vars = filler.split(",")
				attribute = vars[0]
				val1 = vars[1]
				val2 = vars[2]
				outfile.write("\t" * tabs)
				outfile.write("self:set(\"" + attribute + "\", " + val1 + ", " + val2 + ")" + "\n")
			elif f == "chaospoints":
				outfile.write("\t" * tabs)
				outfile.write("other:setflag(4999, other:GetFlag(4999) + " + filler + ")" + "\n")
			elif f == "keepitem":
				outfile.write("\t" * tabs)
				outfile.write("items_table(" + filler + ")" + "\n")
			elif f == "spawnnear":
				filler = do_calcs(filler)
				filler = do_vars(filler)
				npc_id = filler[:int(filler.find(","))]
				time = filler[int(filler.find(","))+1:]
				outfile.write("\t" * tabs)
				outfile.write("spawn(" + npc_id + ", self:GetX() + 3 + math.random(5),self:GetY() + 3 + math.random(5),self:GetZ(),self:GetHeading()," + time + ")" + "\n")
			elif f == "spawnat":
				filler = do_calcs(filler)
				filler = do_vars(filler)
				vars = filler.split(",")
				npc_id = vars[0]
				depop_id = int(vars[1])
				x = vars[2]
				y = vars[3]
				z = vars[4]
				heading = vars[5]
				time = vars[6]
				outfile.write("\t" * tabs)
				outfile.write("spawn(" + npc_id + "," + x + "," + y + "," + z + "," + heading + "," + time + ")" + "\n")
				if depop_id > 0:
					outfile.write("\t" * tabs)
					outfile.write("depop(" + str(depop_id) + ")" + "\n")
			elif f == "cleardebt":
				outfile.write("\t" * tabs)
				outfile.write("other:setexpdebt(0,true)")
			elif f == "removeitem":
				item_id = filler[:int(filler.find(","))]
				amt = int(filler[int(filler.find(","))+1:])
				outfile.write("\t" * tabs)
				outfile.write("inv = other.GetInventory()" + "\n")
				outfile.write("\t" * tabs)
				outfile.write("for i in pairs(inv) do" + "\n")
				tabs = tabs + 1
				outfile.write("\t" * tabs)
				outfile.write("if GetItemID(inv[i]) == " + item_id + " then" + "\n")
				tabs = tabs + 1
				if amt == 0:
					outfile.write("\t" * tabs)
					outfile.write("other:takeitem(inv[i])" + "\n")
				else:
					outfile.write("\t" * tabs)
					outfile.write("inv[i]:reduceitemcharges(" + str(amt) + ")" + "\n")
				tabs = tabs - 1
				outfile.write("\t" * tabs)
				outfile.write("end" + "\n")
				tabs = tabs - 1
				outfile.write("\t" * tabs)
				outfile.write("end" + "\n")
		elif "}" in f:
			tabs = tabs - 1
			if not next_line.startswith("else"):
				outfile.write("\t")
				outfile.write("end" + "\n")
		elif "if" in f:
			if line[2] == " ":
				filler = line[:line.find('(')] + line[line.find('(')+1:line.rfind(')')]
			else:
				filler = line[:line.find('(')] + " " + line[line.find('(')+1:line.rfind(')')]
			filler = do_calcs(filler)
			filler = do_vars(filler)
			outfile.write("\t")
			outfile.write(filler + " then" + "\n")
			tabs = tabs + 1
		else:
			outfile.write("FUNCTION NOT FOUND" + "\n")

if updates_script:
	outfile.write("\t" + "script_status = check_script_status" + "\n")
if updates_s0:
	outfile.write("\t" + "substring_0 = check_substring_0" + "\n")
if updates_s1:
	outfile.write("\t" + "substring_1 = check_substring_1" + "\n")
if updates_s2:
	outfile.write("\t" + "substring_2 = check_substring_2" + "\n")
if updates_s3:
	outfile.write("\t" + "substring_3 = check_substring_3" + "\n")
if updates_s4:
	outfile.write("\t" + "substring_4 = check_substring_4" + "\n")
if updates_s5:
	outfile.write("\t" + "substring_5 = check_substring_5" + "\n")
if updates_s6:
	outfile.write("\t" + "substring_6 = check_substring_6" + "\n")
if updates_s7:
	outfile.write("\t" + "substring_7 = check_substring_7" + "\n")
if updates_s8:
	outfile.write("\t" + "substring_8 = check_substring_8" + "\n")
if updates_s9:
	outfile.write("\t" + "substring_9 = check_substring_9" + "\n")


if EVENT == "SCRIPT" or EVENT == "TRIGGERALL":		
	outfile.write("\t" + "end" + "\n" + "\n")

if EVENT == "SAY" or EVENT == "AGGROSAY":		
	outfile.write("\t" + "end" + "\n" + "\n")

if EVENT == "HP":			
	outfile.write("\t" + "self:hptrigger(self:GetHPTrigger() - 10)" + "\n" + "\n")

outfile.write("end" + "\n" + "\n")


outfile.close()