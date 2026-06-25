from transformers import TrainingArguments

training_args = TrainingArguments(
    output_dir="./results",
    report_to="none"
)

print(training_args.device)
print("Transformers Working")