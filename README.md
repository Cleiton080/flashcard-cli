# Flashcard CLI

The Flashcard CLI is a command-line tool for interacting with your flashcards.

## Using the Flashcard CLI with Docker

Follow these steps to utilize the Flashcard CLI within a Docker environment:

1. **Create a Docker network for the Flashcard CLI:**
   Assuming you're running the API locally using Docker Compose. If not, proceed to step 3 without utilizing the `--network` parameter and adjust `FLASHCARD_BASE_URL` to the base URL where the API is running.
   ```bash
   docker network create flashcard-cli
   ```

2. **Build the Flashcard CLI Docker image:**
   This command builds the Docker image with the flashcard-cli binary.
   ```bash
   docker build -t fc .
   ```

3. **Run the Flashcard CLI:**
   This command runs the container, passing the base URL of the API. If not provided, the default base URL will be http://localhost:5000/api/v1. The `--network` parameter is used to access the API and resolve the passed address correctly. Additionally, a volume is created to maintain user authentication between commands.
   ```bash
   docker run -e FLASHCARD_BASE_URL=http://flashcard-api:5000/api/v1 --network flashcard-cli -v /home/dev/.fc/:/root/.fc -it fc --help
   ```

   The `-e FLASHCARD_BASE_URL=http://flashcard-api:5000/api/v1` option sets the API's base URL.

   The `-it` flag allows interaction within the container's terminal.

4. **Help and available commands:**

   To get help and view the available commands, type:
   ```bash
   fc --help
   ```

   This will display detailed information on how to use the Flashcard CLI.

---

This README serves as a starting point to help you run the Flashcard CLI in Docker. Refer to `fc --help` for more details on available commands and their uses.