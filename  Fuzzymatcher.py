import fuzzymatcher as fm
import pandas as pd

ybox = pd.read_csv(
    'cleanybox.csv'
)
topcv = pd.read_csv(
    'cleantopcv.csv'
)
print(ybox.head(2))
print(topcv.head(2))
left_on = ["title", "company", "city"]
right_on = ["title", "company", "city"]
matched_results = fm.fuzzy_left_join(ybox,
                                    topcv,
                                    left_on,
                                    right_on,
)
cols = [
    "best_match_score", "title_left", "company_left", "date_left", "experience_left",
    "salary_left", "city_left", "specialize", "workingform_left","company_right","title_right","date_right","salary_right",
    "workingform_right","target","position","experience_right","sex","city_right"
]
print(matched_results.head(2))
print(matched_results.columns)
rearranged_best_matches=matched_results[cols].sort_values(by=['best_match_score'], ascending=False)
print(rearranged_best_matches)
# Check the worst 3 matches
rearranged_worst_matches=matched_results[cols].sort_values(by=['best_match_score'],
                                  ascending=True)
print(rearranged_worst_matches.head(3))
# You can also use `tail()` from 'rearranged_best_matches'.
matched_results = matched_results[cols].query("best_match_score <= .75").sort_values(
    by=['best_match_score'], ascending=False)
print(matched_results.head(10))