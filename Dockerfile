# Use a lightweight official Node runtime
FROM node:18-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy package dependency manifests
COPY package*.json ./

# Install project dependencies
RUN npm install --production

# Copy the rest of the application source code
COPY . .

# Expose the port the app runs on (update if needed)
EXPOSE 3080

# Define the command to start the application
CMD ["npm", "start"]
