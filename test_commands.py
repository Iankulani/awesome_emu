#!/usr/bin/env python3
"""
===========================================
AWESOME-EMU-V1 - Command Tests
===========================================
Author: Ian Carter Kulani
Version: 1.0.0

This module contains tests for all commands
"""

import os
import sys
import time
import unittest
import subprocess
import socket
import threading

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import the main module
try:
    from awesome_emu import (
        CommandHandler, DatabaseManager, ConfigManager,
        NetworkTools, PingCommands, TracerouteCommands,
        NmapCommands, CurlCommands, WgetCommands,
        TrafficGeneratorEngine, DOSEngine, SSHManager,
        CrackingEngine, DockerScanner, SocialEngineeringTools,
        Colors
    )
    IMPORTS_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Could not import awesome_emu: {e}")
    IMPORTS_AVAILABLE = False


class TestNetworkTools(unittest.TestCase):
    """Test network tools"""
    
    def setUp(self):
        if not IMPORTS_AVAILABLE:
            self.skipTest("awesome_emu not available")
    
    def test_ping_localhost(self):
        """Test ping to localhost"""
        result = NetworkTools.ping("127.0.0.1", 1)
        self.assertIsInstance(result.success, bool)
        self.assertIsInstance(result.output, str)
        self.assertGreater(result.execution_time, 0)
    
    def test_local_ip(self):
        """Test getting local IP"""
        ip = NetworkTools.get_local_ip()
        self.assertIsNotNone(ip)
        self.assertNotEqual(ip, "")
        # Validate IP format
        parts = ip.split('.')
        self.assertEqual(len(parts), 4)
    
    def test_public_ip(self):
        """Test getting public IP"""
        ip = NetworkTools.get_public_ip()
        if ip:
            parts = ip.split('.')
            self.assertEqual(len(parts), 4)
    
    def test_dns_lookup(self):
        """Test DNS lookup"""
        result = NetworkTools.dns("localhost")
        self.assertIsInstance(result.success, bool)
        self.assertIsInstance(result.output, str)
    
    def test_ip_to_domain(self):
        """Test IP to domain conversion"""
        domain = NetworkTools.ip_to_domain("127.0.0.1")
        # localhost should resolve
        self.assertTrue(domain is None or isinstance(domain, str))
    
    def test_domain_to_ip(self):
        """Test domain to IP conversion"""
        ip = NetworkTools.domain_to_ip("localhost")
        self.assertIsNotNone(ip)
        self.assertEqual(ip, "127.0.0.1")


class TestPingCommands(unittest.TestCase):
    """Test ping commands"""
    
    def setUp(self):
        if not IMPORTS_AVAILABLE:
            self.skipTest("awesome_emu not available")
    
    def test_basic_ping(self):
        """Test basic ping"""
        result = PingCommands.basic("127.0.0.1")
        self.assertIsInstance(result.success, bool)
    
    def test_ping_count(self):
        """Test ping with count"""
        result = PingCommands.count("127.0.0.1", 2)
        self.assertIsInstance(result.success, bool)
    
    def test_ping_size(self):
        """Test ping with size"""
        result = PingCommands.size("127.0.0.1", 64)
        self.assertIsInstance(result.success, bool)
    
    def test_ping_timeout(self):
        """Test ping with timeout"""
        result = PingCommands.timeout("127.0.0.1", 2)
        self.assertIsInstance(result.success, bool)
    
    def test_ping_quiet(self):
        """Test quiet ping"""
        result = PingCommands.quiet("127.0.0.1")
        self.assertIsInstance(result.success, bool)
    
    def test_ping_numeric(self):
        """Test numeric ping"""
        result = PingCommands.numeric("127.0.0.1")
        self.assertIsInstance(result.success, bool)


class TestTracerouteCommands(unittest.TestCase):
    """Test traceroute commands"""
    
    def setUp(self):
        if not IMPORTS_AVAILABLE:
            self.skipTest("awesome_emu not available")
    
    def test_basic_traceroute(self):
        """Test basic traceroute"""
        result = TracerouteCommands.basic("127.0.0.1")
        self.assertIsInstance(result.success, bool)
    
    def test_traceroute_max_hops(self):
        """Test traceroute with max hops"""
        result = TracerouteCommands.max_hops("127.0.0.1", 5)
        self.assertIsInstance(result.success, bool)
    
    def test_traceroute_numeric(self):
        """Test numeric traceroute"""
        result = TracerouteCommands.numeric("127.0.0.1")
        self.assertIsInstance(result.success, bool)
    
    def test_traceroute_wait(self):
        """Test traceroute with wait"""
        result = TracerouteCommands.wait("127.0.0.1", 1)
        self.assertIsInstance(result.success, bool)


class TestNmapCommands(unittest.TestCase):
    """Test nmap commands"""
    
    def setUp(self):
        if not IMPORTS_AVAILABLE:
            self.skipTest("awesome_emu not available")
    
    def test_nmap_version(self):
        """Test nmap version"""
        result = NmapCommands.version()
        self.assertIsInstance(result.output, str)
    
    def test_nmap_help(self):
        """Test nmap help"""
        result = NmapCommands.help()
        self.assertIsInstance(result.output, str)
    
    def test_nmap_quick(self):
        """Test quick nmap scan"""
        result = NmapCommands.quick("127.0.0.1")
        self.assertIsInstance(result.success, bool)
    
    def test_nmap_ping_scan(self):
        """Test nmap ping scan"""
        result = NmapCommands.ping_scan("127.0.0.1")
        self.assertIsInstance(result.success, bool)
    
    def test_nmap_fast(self):
        """Test fast nmap scan"""
        result = NmapCommands.fast_scan("127.0.0.1")
        self.assertIsInstance(result.success, bool)
    
    def test_nmap_iflist(self):
        """Test nmap interface list"""
        result = NmapCommands.iflist()
        self.assertIsInstance(result.success, bool)
    
    def test_nmap_top_ports(self):
        """Test nmap top ports"""
        result = NmapCommands.top_ports("127.0.0.1", 10)
        self.assertIsInstance(result.success, bool)


class TestCurlCommands(unittest.TestCase):
    """Test curl commands"""
    
    def setUp(self):
        if not IMPORTS_AVAILABLE:
            self.skipTest("awesome_emu not available")
    
    def test_curl_version(self):
        """Test curl version"""
        result = CurlCommands.version()
        self.assertIsInstance(result.output, str)
    
    def test_curl_help(self):
        """Test curl help"""
        result = CurlCommands.help()
        self.assertIsInstance(result.output, str)
    
    def test_curl_get(self):
        """Test curl GET request"""
        result = CurlCommands.get("http://httpbin.org/get")
        self.assertIsInstance(result.success, bool)
    
    def test_curl_ipv4(self):
        """Test curl IPv4"""
        result = CurlCommands.ipv4("http://httpbin.org/ip")
        self.assertIsInstance(result.success, bool)


class TestWgetCommands(unittest.TestCase):
    """Test wget commands"""
    
    def setUp(self):
        if not IMPORTS_AVAILABLE:
            self.skipTest("awesome_emu not available")
    
    def test_wget_version(self):
        """Test wget version"""
        result = WgetCommands.version()
        self.assertIsInstance(result.output, str)
    
    def test_wget_help(self):
        """Test wget help"""
        result = WgetCommands.help()
        self.assertIsInstance(result.output, str)
    
    def test_wget_spider(self):
        """Test wget spider"""
        result = WgetCommands.spider("http://httpbin.org")
        self.assertIsInstance(result.success, bool)


class TestCommandHandler(unittest.TestCase):
    """Test command handler"""
    
    @classmethod
    def setUpClass(cls):
        if not IMPORTS_AVAILABLE:
            cls.skipTest("awesome_emu not available")
        cls.config = ConfigManager()
        cls.db = DatabaseManager(":memory:")
        cls.handler = CommandHandler(cls.db, cls.config)
    
    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'db'):
            cls.db.close()
    
    def test_help_command(self):
        """Test help command"""
        result = self.handler.execute("help")
        self.assertTrue(result['success'])
        self.assertIn("PING COMMANDS", result['output'])
    
    def test_status_command(self):
        """Test status command"""
        result = self.handler.execute("status")
        self.assertTrue(result['success'])
        self.assertIn("Statistics", result['output'])
    
    def test_version_command(self):
        """Test version command"""
        result = self.handler.execute("version")
        self.assertTrue(result['success'])
        self.assertIn("1.0.0", result['output'])
    
    def test_system_command(self):
        """Test system command"""
        result = self.handler.execute("system")
        self.assertTrue(result['success'])
        self.assertIn("System Information", result['output'])
    
    def test_threats_command(self):
        """Test threats command"""
        result = self.handler.execute("threats")
        self.assertTrue(result['success'])
    
    def test_history_command(self):
        """Test history command"""
        result = self.handler.execute("history")
        self.assertTrue(result['success'])
    
    def test_ping_command(self):
        """Test ping command"""
        result = self.handler.execute("ping 127.0.0.1")
        self.assertIsInstance(result['success'], bool)
    
    def test_ping_count_command(self):
        """Test ping_count command"""
        result = self.handler.execute("ping_count 127.0.0.1 2")
        self.assertIsInstance(result['success'], bool)
    
    def test_traceroute_command(self):
        """Test traceroute command"""
        result = self.handler.execute("traceroute 127.0.0.1")
        self.assertIsInstance(result['success'], bool)
    
    def test_nmap_quick_command(self):
        """Test nmap_quick command"""
        result = self.handler.execute("nmap_quick 127.0.0.1")
        self.assertIsInstance(result['success'], bool)
    
    def test_nmap_version_command(self):
        """Test nmap_version command"""
        result = self.handler.execute("nmap_version")
        self.assertTrue(result['success'])
    
    def test_curl_version_command(self):
        """Test curl_version command"""
        result = self.handler.execute("curl_version")
        self.assertTrue(result['success'])
    
    def test_wget_version_command(self):
        """Test wget_version command"""
        result = self.handler.execute("wget_version")
        self.assertTrue(result['success'])
    
    def test_dns_command(self):
        """Test dns command"""
        result = self.handler.execute("dns localhost")
        self.assertIsInstance(result['success'], bool)
    
    def test_location_command(self):
        """Test location command"""
        result = self.handler.execute("location 8.8.8.8")
        self.assertIsInstance(result['success'], bool)
    
    def test_ip_info_command(self):
        """Test ip_info command"""
        result = self.handler.execute("ip_info 8.8.8.8")
        self.assertIsInstance(result['success'], bool)
    
    def test_add_ip_command(self):
        """Test add_ip command"""
        result = self.handler.execute("add_ip 192.168.1.100 test")
        self.assertTrue(result['success'])
    
    def test_list_ips_command(self):
        """Test list_ips command"""
        result = self.handler.execute("list_ips")
        self.assertTrue(result['success'])
    
    def test_traffic_types_command(self):
        """Test traffic_types command"""
        result = self.handler.execute("traffic_types")
        self.assertTrue(result['success'])
        self.assertIn("Available traffic types", result['output'])
    
    def test_dos_status_command(self):
        """Test dos_status command"""
        result = self.handler.execute("dos_status")
        self.assertTrue(result['success'])
    
    def test_keylogger_status_command(self):
        """Test keylogger_status command"""
        result = self.handler.execute("keylogger_status")
        self.assertIsInstance(result['success'], bool)
    
    def test_crack_list_command(self):
        """Test crack_list command"""
        result = self.handler.execute("crack_list")
        self.assertTrue(result['success'])
    
    def test_phish_list_command(self):
        """Test phish_list command"""
        result = self.handler.execute("phish_list")
        self.assertTrue(result['success'])
    
    def test_phish_gmail_command(self):
        """Test phish_gmail command"""
        result = self.handler.execute("phish_gmail")
        self.assertIsInstance(result['success'], bool)
    
    def test_invalid_command(self):
        """Test invalid command"""
        result = self.handler.execute("invalid_command_xyz")
        # Should not crash
        self.assertIsInstance(result, dict)


class TestDatabaseManager(unittest.TestCase):
    """Test database manager"""
    
    def setUp(self):
        if not IMPORTS_AVAILABLE:
            self.skipTest("awesome_emu not available")
        self.db = DatabaseManager(":memory:")
    
    def tearDown(self):
        if hasattr(self, 'db'):
            self.db.close()
    
    def test_log_command(self):
        """Test logging a command"""
        self.db.log_command("test command", "test", success=True)
        history = self.db.conn.execute(
            "SELECT * FROM command_history WHERE command = 'test command'"
        ).fetchall()
        self.assertEqual(len(history), 1)
    
    def test_log_threat(self):
        """Test logging a threat"""
        self.db.log_threat("port_scan", "192.168.1.1", "medium", "Port scan detected")
        threats = self.db.get_recent_threats(1)
        self.assertEqual(len(threats), 1)
        self.assertEqual(threats[0]['threat_type'], "port_scan")
    
    def test_add_managed_ip(self):
        """Test adding managed IP"""
        result = self.db.add_managed_ip("10.0.0.1", "example.com", "test", "Test IP")
        self.assertTrue(result)
        ips = self.db.get_managed_ips()
        self.assertTrue(any(ip['ip_address'] == "10.0.0.1" for ip in ips))
    
    def test_block_unblock_ip(self):
        """Test blocking and unblocking IP"""
        self.db.add_managed_ip("10.0.0.2")
        self.db.block_ip("10.0.0.2", "Test block")
        ips = self.db.get_managed_ips()
        blocked = [ip for ip in ips if ip['ip_address'] == "10.0.0.2"]
        self.assertTrue(blocked[0]['is_blocked'])
        
        self.db.unblock_ip("10.0.0.2")
        ips = self.db.get_managed_ips()
        unblocked = [ip for ip in ips if ip['ip_address'] == "10.0.0.2"]
        self.assertFalse(unblocked[0]['is_blocked'])
    
    def test_save_keylog(self):
        """Test saving keylog"""
        self.db.save_keylog("test keylog", "Test Window", "test.exe")
        logs = self.db.get_keylogs(1)
        self.assertEqual(len(logs), 1)
        self.assertEqual(logs[0]['text'], "test keylog")
    
    def test_get_statistics(self):
        """Test getting statistics"""
        stats = self.db.get_statistics()
        self.assertIsInstance(stats, dict)
        self.assertIn('total_commands', stats)
        self.assertIn('total_threats', stats)


class TestConfigManager(unittest.TestCase):
    """Test config manager"""
    
    def setUp(self):
        if not IMPORTS_AVAILABLE:
            self.skipTest("awesome_emu not available")
        self.config = ConfigManager()
    
    def test_get_default(self):
        """Test getting default config"""
        version = self.config.get('version')
        self.assertEqual(version, "1.0.0")
    
    def test_get_nested(self):
        """Test getting nested config"""
        port = self.config.get('web.port')
        self.assertEqual(port, 5000)
    
    def test_set_config(self):
        """Test setting config"""
        self.config.set('test.value', 123)
        self.assertEqual(self.config.get('test.value'), 123)


class TestTrafficGenerator(unittest.TestCase):
    """Test traffic generator"""
    
    def setUp(self):
        if not IMPORTS_AVAILABLE:
            self.skipTest("awesome_emu not available")
        self.db = DatabaseManager(":memory:")
        self.generator = TrafficGeneratorEngine(self.db)
    
    def tearDown(self):
        self.generator.stop()
        self.db.close()
    
    def test_get_available_types(self):
        """Test getting available traffic types"""
        types = self.generator.get_available_types()
        self.assertIsInstance(types, list)
        self.assertIn('icmp', types)
        self.assertIn('udp', types)
        self.assertIn('tcp_syn', types)
    
    def test_invalid_ip(self):
        """Test invalid IP handling"""
        with self.assertRaises(ValueError):
            self.generator.generate("icmp", "invalid_ip", 1)


class TestDOSEngine(unittest.TestCase):
    """Test DOS engine"""
    
    def setUp(self):
        if not IMPORTS_AVAILABLE:
            self.skipTest("awesome_emu not available")
        self.db = DatabaseManager(":memory:")
        self.config = ConfigManager()
        self.dos = DOSEngine(self.db, self.config)
    
    def tearDown(self):
        self.dos.stop()
        self.db.close()
    
    def test_invalid_ip(self):
        """Test invalid IP handling"""
        result = self.dos.syn_flood("invalid_ip", 80, 1)
        self.assertFalse(result['success'])
    
    def test_get_active(self):
        """Test getting active attacks"""
        active = self.dos.get_active()
        self.assertIsInstance(active, list)


class TestCrackingEngine(unittest.TestCase):
    """Test cracking engine"""
    
    def setUp(self):
        if not IMPORTS_AVAILABLE:
            self.skipTest("awesome_emu not available")
        self.db = DatabaseManager(":memory:")
        self.config = ConfigManager()
        self.cracking = CrackingEngine(self.db, self.config)
    
    def tearDown(self):
        self.db.close()
    
    def test_md5_crack(self):
        """Test MD5 cracking"""
        # Create test wordlist
        wordlist = "/tmp/test_wordlist.txt"
        with open(wordlist, 'w') as f:
            f.write("password\n123456\ntest\n")
        
        # MD5 of "test"
        md5_hash = "098f6bcd4621d373cade4e832627b4f6"
        job_id = self.cracking.crack_hash("md5", md5_hash, wordlist)
        self.assertIsNotNone(job_id)
    
    def test_get_all_jobs(self):
        """Test getting all jobs"""
        jobs = self.cracking.get_all_jobs()
        self.assertIsInstance(jobs, list)


class TestSocialEngineering(unittest.TestCase):
    """Test social engineering tools"""
    
    def setUp(self):
        if not IMPORTS_AVAILABLE:
            self.skipTest("awesome_emu not available")
        self.db = DatabaseManager(":memory:")
        self.social = SocialEngineeringTools(self.db)
    
    def tearDown(self):
        self.social.stop_server()
        self.db.close()
    
    def test_templates_loaded(self):
        """Test templates are loaded"""
        self.assertIsInstance(self.social.templates, dict)
        self.assertGreater(len(self.social.templates), 100)
    
    def test_generate_phishing_link(self):
        """Test generating phishing link"""
        result = self.social.generate_phishing_link("gmail")
        self.assertTrue(result['success'])
        self.assertIn('link_id', result)
    
    def test_get_captured_credentials(self):
        """Test getting captured credentials"""
        creds = self.social.get_captured_credentials()
        self.assertIsInstance(creds, list)


class TestDockerScanner(unittest.TestCase):
    """Test Docker scanner"""
    
    def setUp(self):
        if not IMPORTS_AVAILABLE:
            self.skipTest("awesome_emu not available")
        self.db = DatabaseManager(":memory:")
        self.docker = DockerScanner(self.db)
    
    def tearDown(self):
        self.db.close()
    
    def test_docker_info(self):
        """Test docker info"""
        result = self.docker.docker_info()
        self.assertIsInstance(result['success'], bool)
    
    def test_docker_ps(self):
        """Test docker ps"""
        result = self.docker.docker_ps()
        self.assertIsInstance(result['success'], bool)


class TestIntegration(unittest.TestCase):
    """Integration tests"""
    
    def setUp(self):
        if not IMPORTS_AVAILABLE:
            self.skipTest("awesome_emu not available")
        self.config = ConfigManager()
        self.db = DatabaseManager(":memory:")
        self.handler = CommandHandler(self.db, self.config)
    
    def tearDown(self):
        self.db.close()
    
    def test_full_workflow(self):
        """Test a full workflow"""
        # Add IP
        result = self.handler.execute("add_ip 192.168.1.200 test")
        self.assertTrue(result['success'])
        
        # List IPs
        result = self.handler.execute("list_ips")
        self.assertTrue(result['success'])
        self.assertIn("192.168.1.200", result['output'])
        
        # Block IP
        result = self.handler.execute("block_ip 192.168.1.200 test block")
        self.assertIsInstance(result['success'], bool)
        
        # Get stats
        result = self.handler.execute("status")
        self.assertTrue(result['success'])
        
        # Check history
        result = self.handler.execute("history 5")
        self.assertTrue(result['success'])


def run_all_tests():
    """Run all tests"""
    print(f"\n{Colors.BRIGHT_WHITE}{'='*60}{Colors.RESET}")
    print(f"{Colors.BRIGHT_CYAN}🧪 AWESOME-EMU-V1 - Test Suite{Colors.RESET}")
    print(f"{Colors.BRIGHT_WHITE}{'='*60}{Colors.RESET}\n")
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    test_classes = [
        TestNetworkTools,
        TestPingCommands,
        TestTracerouteCommands,
        TestNmapCommands,
        TestCurlCommands,
        TestWgetCommands,
        TestCommandHandler,
        TestDatabaseManager,
        TestConfigManager,
        TestTrafficGenerator,
        TestDOSEngine,
        TestCrackingEngine,
        TestSocialEngineering,
        TestDockerScanner,
        TestIntegration
    ]
    
    for test_class in test_classes:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print(f"\n{Colors.BRIGHT_WHITE}{'='*60}{Colors.RESET}")
    print(f"{Colors.BRIGHT_CYAN}📊 Test Summary{Colors.RESET}")
    print(f"{Colors.BRIGHT_WHITE}{'='*60}{Colors.RESET}")
    print(f"  Tests Run: {result.testsRun}")
    print(f"  {Colors.SUCCESS}Passed: {result.testsRun - len(result.failures) - len(result.errors)}{Colors.RESET}")
    print(f"  {Colors.ERROR}Failed: {len(result.failures)}{Colors.RESET}")
    print(f"  {Colors.ERROR}Errors: {len(result.errors)}{Colors.RESET}")
    print(f"  {Colors.WARNING}Skipped: {len(result.skipped)}{Colors.RESET}")
    print(f"{Colors.BRIGHT_WHITE}{'='*60}{Colors.RESET}\n")
    
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(run_all_tests())
