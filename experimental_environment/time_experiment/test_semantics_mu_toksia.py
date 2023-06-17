from record_time import record_time_mu_toksia

# Directory containing the generated test frameworks
DIRECTORY = 'examples'

# Do the check for the stable semantics encoding
record_time_mu_toksia("Preferred", "PR", DIRECTORY)
record_time_mu_toksia("Stable", "ST", DIRECTORY)
record_time_mu_toksia("Complete", "CO", DIRECTORY)