from constants import ADMISSIBLE_ASP, ADMISSIBLE_ASPARTIX, STABLE_ASP, STABLE_ASPARTIX, COMPLETE_ASP, COMPLETE_ASPARTIX, PREFERRED_ASP, PREFERRED_ASPARTIX, GROUNDED_ASP, GROUNDED_ASPARTIX
from check_consistency import check_consistency, check_consistency_no_aspartix_base

# Directory containing the generated test frameworks
DIRECTORY = 'examples_1000'

# Do the check for the stable semantics encoding
stable_result = check_consistency(STABLE_ASP, STABLE_ASPARTIX, "Stable", DIRECTORY)
print(
    f"The number of consistent files is: {stable_result[0]} out of {stable_result[1]}")
print("---------------------------------------------")

# Do the check for the complete semantics encoding
complete_result = check_consistency(
    COMPLETE_ASP, COMPLETE_ASPARTIX, "Complete", DIRECTORY)
print(
    f"The number of consistent files is: {complete_result[0]} out of {complete_result[1]}")
print("---------------------------------------------")

# Do the check for the admissible semantics encoding
admissible_result = check_consistency(
    ADMISSIBLE_ASP, ADMISSIBLE_ASPARTIX, "Admissible", DIRECTORY)
print(
    f"The number of consistent files is: {admissible_result[0]} out of {admissible_result[1]}")
print("---------------------------------------------")

# Do the check for the preferred semantics encoding
preferred_result = check_consistency_no_aspartix_base(
    PREFERRED_ASP, PREFERRED_ASPARTIX, "Preferred", DIRECTORY)
print(
    f"The number of consistent files is: {preferred_result[0]} out of {preferred_result[1]}")
print("---------------------------------------------")

# Do the check for the grounded semantics encoding
grounded_result = check_consistency_no_aspartix_base(
    GROUNDED_ASP, GROUNDED_ASPARTIX, "Grounded", DIRECTORY)
print(
    f"The number of consistent files is: {grounded_result[0]} out of {grounded_result[1]}")
print("---------------------------------------------")