
import pandas


input_file_name = "gsr-session-responses-08-03-18"
gsr_responses_df = pandas.read_csv(input_file_name + ".csv")
gsr_responses_df["MondaySession"] = ""
gsr_responses_df["TuesdaySession"] = ""


gsr_responses_df.head(2)

{"A" : {"count" : 0, "max" : 75, "names" : []}, 
 "B" : {"count" : 0, "max" : 40, "names" : []}, 
 "C" : {"count" : 0, "max" : 30, "names" : []},
 "D" : {"count" : 0, "max" : 30, "names" : []}}

mon_session_counter = {"A" : {"count" : 0, "max" : 80, "names" : []}, 
 "B" : {"count" : 0, "max" : 80, "names" : []}, 
 "C" : {"count" : 0, "max" : 80, "names" : []},
 "D" : {"count" : 0, "max" : 80, "names" : []}}
tue_session_counter_codeu = {"A" : {"count" : 0, "max" : 80, "names" : []}, 
 "B" : {"count" : 0, "max" : 80, "names" : []}, 
 "C" : {"count" : 0, "max" : 80, "names" : []},
 "D" : {"count" : 0, "max" : 80, "names" : []}}
tue_session_counter_sch = {"A" : {"count" : 0, "max" : 18, "names" : []}, 
 "B" : {"count" : 0, "max" : 18, "names" : []}, 
 "C" : {"count" : 0, "max" : 18, "names" : []},
 "D" : {"count" : 0, "max" : 18, "names" : []}}


def check_bucket(session_counter, pref, student_name, output_col_name):
    if session_counter[pref]['count'] < mon_session_counter[pref]['max']:
        session_counter[pref]['count'] = mon_session_counter[pref]['count'] + 1
        session_counter[pref]['names'].append(student_name)
        row[output_col_name] = pref
        return True
    else:
        return False

        
sessions = {"mon" : mon_session_counter, 
            "tues": {"codeu_tues" : tue_session_counter_codeu,
                    "sch_tues" : tue_session_counter_sch }}
for index, row in gsr_responses_df.iterrows():
    full_name = row["First Name"] + " " + row["Last Name"]
    mon_first = row["Monday first preference"][0]
    if not check_bucket(mon_session_counter, mon_first, full_name, "MondaySession"):
        mon_second = row["Monday second preference"][0]
        if not check_bucket(mon_session_counter, mon_second, full_name, "MondaySession"):
            print("Preferences full for " + full_name + "on Monday")
    
    if row["Which program are you joining from?"] == "CodeU":
        if(pandas.isnull(row["Tuesday first preference (CodeU)"])):
            print(full_name + " did not mark Tuesday preference (CodeU)")
        else:    
            tue_first = row["Tuesday first preference (CodeU)"][0]
            if not check_bucket(tue_session_counter_codeu, tue_first, full_name, "TuesdaySession"):
                tue_second = row["Tuesday second preference (CodeU)"][0] 
                if not check_bucket(tue_session_counter_codeu, tue_second, full_name, "TuesdaySession"):
                    "Preferences full for " + full_name + "on Tuesday (CodeU)"
    else:
        if(pandas.isnull(row["Tuesday first preference (Scholars)"])):
            print(full_name + " did not mark Tuesday preference (Scholars)")
        else:    
            tue_first = row["Tuesday first preference (Scholars)"][0]
            if not check_bucket(tue_session_counter_sch, tue_first, full_name, "TuesdaySession"):
                tue_second = row["Tuesday second preference (Scholars)"][0] 
                if not check_bucket(tue_session_counter_sch, tue_second, full_name, "TuesdaySession"):
                    "Preferences full for " + full_name + "on Tuesday (Scholars)"
    
    
#print(sessions)

#gsr_responses_df.to_csv(input_file_name+"_slotted.csv")
