from constants import ADMISSIBLE_ASP, ADMISSIBLE_ASPARTIX, STABLE_ASP, STABLE_ASPARTIX, COMPLETE_ASP, COMPLETE_ASPARTIX, PREFERRED_ASP, PREFERRED_ASPARTIX, GROUNDED_ASP, GROUNDED_ASPARTIX
from record_time import record_time, record_time_no_aspartix_base

# Directory containing the generated test frameworks
DIRECTORY = 'examples'

# Print how much time it takes to find an extension for each semantics 
record_time_no_aspartix_base(PREFERRED_ASP, PREFERRED_ASPARTIX, "Preferred", DIRECTORY)

record_time_no_aspartix_base(GROUNDED_ASP, GROUNDED_ASPARTIX, "Grounded", DIRECTORY)

record_time(STABLE_ASP, STABLE_ASPARTIX, "Stable", DIRECTORY)

record_time(COMPLETE_ASP, COMPLETE_ASPARTIX, "Complete", DIRECTORY)

record_time(ADMISSIBLE_ASP, ADMISSIBLE_ASPARTIX, "Admissible", DIRECTORY)