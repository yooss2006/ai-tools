#!/usr/bin/env node
import { Command } from 'commander';

const program = new Command();

program
  .name('json-csv')
  .description('Convert a JSON array file to CSV')
  .argument('<input>', 'path to a JSON file containing an array of objects')
  .requiredOption('-o, --output <path>', 'path for the generated CSV file');

program.parse();
