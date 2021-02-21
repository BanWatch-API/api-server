#Import required dependencies first
import asyncio
import os
import sys
import time
from fastapi import Depends, FastAPI, HTTPException, status
import spamwatch
