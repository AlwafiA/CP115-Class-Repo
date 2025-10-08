applicant_age = int(input())
vision_test = input()
written_score = int(input())
driving_score = int(input())
medical_clearance = input()

# Check if each individual requirement is met
is_age_for_class_A = applicant_age >= 21
is_age_for_class_B = applicant_age >= 18
passed_vision = vision_test == "Pass"
passed_written = written_score >= 80
passed_driving = driving_score >= 85
passed_medical = medical_clearance == "Pass"

# Check for the license class in hierarchical order (strictest first)
if is_age_for_class_A and passed_vision and passed_written and passed_driving and passed_medical:

    license_class = "Class A (Commercial)"
elif is_age_for_class_B and passed_vision and passed_written and passed_driving:

    license_class = "Class B (Regular)"
else:

    tests_passed_count = int(passed_vision) + int(passed_written) + int(passed_driving) + int(passed_medical)

    if tests_passed_count >= 2:

        license_class = "Restricted License"
    else:

        license_class = "Application Denied"

print(license_class)