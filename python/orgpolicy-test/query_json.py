import re

error_message = "400 The request has violated one or more Org Policies. Please refer to the respective violations for more information. [violations {\n"\
                "type: \"constraints/cloudfunctions.allowed/pcConnectorEgressSettings\"\n"\
                "subject: \"orgpolicy:projects/pri-iam-denytest\"\n"\
                "description: *Constraint constraints/cloudfunctions. allowed/pcConnectorEgresssettings violated for projects/prj-iam-denytest attempting CreateFunctionActionV with vpc_connector _egress _detting\n"\
                "5 set to VPC CONNECTOR EGRESS SETTINGS UNSPECIFIED. See https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints for more information.\"\n"\
                "description: *Another description field\n"\
                "}] ** message-> The request has violated one or more Org Policies. Please refer to the respective violations for more information."

# Using regular expression to find all description fields
description_pattern = r"description: \"(.*?)\""
description_matches = re.findall(description_pattern, error_message)
if description_matches:
    for index, description_value in enumerate(description_matches, start=1):
        print(f"Description {index}: {description_value}")
else:
    print("No description fields found.")
