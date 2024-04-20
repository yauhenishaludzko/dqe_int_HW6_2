import great_expectations as ge
from great_expectations.profile.user_configurable_profiler import UserConfigurableProfiler

# Define columns skipped by profiler
ignored_columns = []

# Define batch request parameters
batch_request_parameters = {
    "datasource_name": "pv_datasource",
    "data_connector_name": "default_configured_data_connector_name",
    "data_asset_name": "employees"
}

# Create a DataContext
context = ge.data_context.DataContext()

# Create a BatchRequest object
batch_request = ge.core.batch.BatchRequest(**batch_request_parameters)

# Get the validator from the DataContext
validator = context.get_validator(batch_request=batch_request)

# Create a profiler and pass the validator
profiler = UserConfigurableProfiler(profile_dataset=validator, ignored_columns=ignored_columns)

# Automatically build the suite
profiler.build_suite()

# Save the expectation suite with a custom name
validator.save_expectation_suite()

# Explore Data Docs (optional)
context.build_data_docs()
context.open_data_docs()

# Create a checkpoint
checkpoint_name = "checkpoint_Employee"
checkpoint = context.add_or_update_checkpoint(
    name=checkpoint_name,
    batch_request=batch_request,
    expectation_suite_name="hr_employees")

# Run the checkpoint to validate the data
checkpoint_result = checkpoint.run()

# Explore Data Docs
context.build_data_docs()
context.open_data_docs()


