#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { AgentsCdkStack } from '../lib/agents-cdk-stack';

const app = new cdk.App();
new AgentsCdkStack(app, 'AgentsCdkStack', {
  env: { account: '532805286864', region: 'us-east-1' }
});