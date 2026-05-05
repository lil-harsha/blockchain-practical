// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract DocumentRegistry {
    struct Document {
        address owner;
        uint256 timestamp;
        string description;
        bool exists;
    }

    mapping(bytes32 => Document) private documents;

    event DocumentRegistered(
        bytes32 indexed docHash,
        address indexed owner,
        uint256 timestamp,
        string description
    );

    function computeSHA256(string calldata text) external pure returns (bytes32) {
        return sha256(bytes(text));
    }

    function registerDocument(bytes32 docHash, string calldata description) external {
        require(docHash != bytes32(0), "Invalid hash");
        require(!documents[docHash].exists, "Document already registered");

        documents[docHash] = Document({
            owner: msg.sender,
            timestamp: block.timestamp,
            description: description,
            exists: true
        });

        emit DocumentRegistered(docHash, msg.sender, block.timestamp, description);
    }

    function isRegistered(bytes32 docHash) external view returns (bool) {
        return documents[docHash].exists;
    }

    function getDocument(bytes32 docHash)
        external
        view
        returns (bool exists, address owner, uint256 timestamp, string memory description)
    {
        Document memory d = documents[docHash];
        return (d.exists, d.owner, d.timestamp, d.description);
    }
}
