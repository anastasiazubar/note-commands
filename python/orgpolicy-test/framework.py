@when('split constraint violations by compute')
def step_impl(context):
    response = context.response  # or wherever your raw error is stored
    split_parts = response.split("constraint constraints/compute")

    # Reattach the split keyword and filter useful parts
    violations = [
        f"constraint constraints/compute{part.strip().split()[0]}"
        for part in split_parts[1:]  # skip the first chunk (before first match)
    ]

    # Log or print the violations
    LOGGER.info("\nSplit constraint violations:")
    for v in violations:
        print(f"- {v}")

    # Optional: store it in context for later steps
    context.violations = violations
