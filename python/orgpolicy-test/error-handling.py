    except Exception as err:
        # Catch and handle "IAM_PERMISSION_DENIED"
        if "IAM_PERMISSION_DENIED" in str(err):
            LOGGER.info(f"IAM_PERMISSION_DENIED occurred: {err}")
            context.response = "IAM_PERMISSION_DENIED: " + str(err).split("\n", 1)[0]
        else:
            # Re-raise unexpected exceptions
            raise err