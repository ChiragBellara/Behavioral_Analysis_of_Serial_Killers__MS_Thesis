import re


def read_text_to_list(filename):
    transcript = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            transcript.append(line)
    return transcript


def convert_to_seconds(timestamp):
    """Converts a timestamp (HH:MM:SS) to seconds."""
    h, m, s = map(int, timestamp.split(':'))
    return h * 3600 + m * 60 + s


def format_transcript(transcript):
    formatted = []
    with open("Elizabeth_pyconverse.csv", 'w') as fw:
        for i, line in enumerate(transcript):
            # Extract timestamp, speaker, and text using regex
            match = re.match(r"(\d{2}:\d{2}:\d{2}) (\w+ \d+) (.+)", line)
            if not match:
                continue
            start_time, speaker, text = match.groups()

            # Calculate start time in seconds
            start_seconds = convert_to_seconds(start_time)

            # Determine the end time
            if i + 1 < len(transcript):
                next_start_time = transcript[i + 1].split()[0]
                end_seconds = convert_to_seconds(next_start_time)
                end_seconds_str = f"{end_seconds:.3f}"
            else:
                end_seconds_str = ""

            text = f'"{text.strip()}"'

            # Format line
            formatted_line = f"{
                i + 1},{speaker},{text},{start_seconds:.3f},{end_seconds_str}"
            formatted.append(formatted_line)

            fw.write(formatted_line + "\n")
    fw.close()
    return formatted


transcript = read_text_to_list('Elizabeth.txt')
print(transcript[10])

# Process the transcript
formatted_transcript = format_transcript(transcript)

# Print the output
for line in formatted_transcript:
    print(line)
