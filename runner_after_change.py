import great_expectations as ge

# Create a DataContext
context = ge.data_context.DataContext()

# Specify the name of the expectation suite you want to validate against
expectation_suite_name = "hr_employees"

# Load the expectation suite
expectation_suite = context.get_expectation_suite(expectation_suite_name)

# Specify the batch request parameters
batch_request_parameters = {
    "datasource_name": "pv_datasource",
    "data_connector_name": "default_configured_data_connector_name",
    "data_asset_name": "employees"
}

# Create a BatchRequest object
batch_request = ge.core.batch.BatchRequest(**batch_request_parameters)

# Create a checkpoint
checkpoint_name = "checkpoint_employees_changed"
checkpoint = context.add_or_update_checkpoint(
    name=checkpoint_name,
    batch_request=batch_request,
    expectation_suite_name="hr_employees")


# Run the checkpoint to validate the data
checkpoint_result = checkpoint.run()

# Optionally, you can also generate and explore Data Docs
context.build_data_docs()
context.open_data_docs()
