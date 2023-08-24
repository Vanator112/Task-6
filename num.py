def process_file(input_file, output_file):
    numbers = []

    with open(input_file, 'r') as input:
        for line in input:
            num = int(line.strip())
            num_str = str(num)
            found = num_str.find("123")

            while found != -1:
                num_str = num_str.replace("123", "321", 1)
                found = num_str.find("123")

            try:
                modified_num = int(num_str)
                numbers.append(modified_num)
            except ValueError:
                pass  # Ignore invalid numbers

    numbers.sort()

    with open(output_file, 'w') as output:
        for n in numbers:
            output.write(str(n) + '\n')

    print(f"Processed input from '{input_file}' and wrote results to '{output_file}'.")

if __name__ == "__main__":
    process_file("data.in", "data.out")

