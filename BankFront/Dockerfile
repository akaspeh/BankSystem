# Use an official Node.js image as a base image
FROM node:14 as builder

# Set the working directory inside the container
WORKDIR /BankFront

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Build Angular code
RUN npm run build

# Use Nginx to serve the Angular app in a lightweight container
FROM nginx:alpine

# Copy the built Angular app from the builder stage to the nginx directory
COPY --from=builder /BankFront/dist /usr/share/nginx/html

# Expose the default Nginx port
EXPOSE 80
