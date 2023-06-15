    def test_set_iam_policy(self):
        import operator
        from google.cloud.storage.iam import STORAGE_OWNER_ROLE
        from google.cloud.storage.iam import STORAGE_EDITOR_ROLE
        from google.cloud.storage.iam import STORAGE_VIEWER_ROLE
        from google.api_core.iam import Policy

        blob_name = "blob-name"
        path = f"/b/name/o/{blob_name}"
        etag = "DEADBEEF"
        version = 1
        owner1 = "user:phred@example.com"
        owner2 = "group:cloud-logs@google.com"
        editor1 = "domain:google.com"
        editor2 = "user:phred@example.com"
        viewer1 = "serviceAccount:1234-abcdef@service.example.com"
        viewer2 = "user:phred@example.com"
        bindings = [
            {"role": STORAGE_OWNER_ROLE, "members": [owner1, owner2]},
            {"role": STORAGE_EDITOR_ROLE, "members": [editor1, editor2]},
            {"role": STORAGE_VIEWER_ROLE, "members": [viewer1, viewer2]},
        ]
        api_response = {"etag": etag, "version": version, "bindings": bindings}
        policy = Policy()
        for binding in bindings:
            policy[binding["role"]] = binding["members"]

        client = mock.Mock(spec=["_put_resource"])
        client._put_resource.return_value = api_response
        bucket = _Bucket(client=client)
        blob = self._make_one(blob_name, bucket=bucket)

        returned = blob.set_iam_policy(policy)

        self.assertEqual(returned.etag, etag)
        self.assertEqual(returned.version, version)
        self.assertEqual(dict(returned), dict(policy))

        expected_path = f"{path}/iam"
        expected_data = {
            "resourceId": path,
            "bindings": mock.ANY,
        }
        expected_query_params = {}
        client._put_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_ETAG_IN_JSON,
            _target_object=None,
        )

        sent_bindings = client._put_resource.call_args.args[1]["bindings"]
        key = operator.itemgetter("role")
        for found, expected in zip(
            sorted(sent_bindings, key=key), sorted(bindings, key=key)
        ):
            self.assertEqual(found["role"], expected["role"])
            self.assertEqual(sorted(found["members"]), sorted(expected["members"]))
